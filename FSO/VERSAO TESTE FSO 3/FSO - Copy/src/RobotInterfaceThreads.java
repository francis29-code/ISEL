
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.concurrent.Semaphore;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;


public class RobotInterfaceThreads extends JFrame implements ILogger{
	private static final long serialVersionUID = 1L;
	
	private JPanel contentPane;
	private JTextField robotNameText;
	private JRadioButton rdbtnOnoff;
	private JCheckBox chckbxDebug;
	private JCheckBox chckbxHandler;
	private JCheckBox chckbxEvitar;
	private JCheckBox chckbxWander;
	private JTextField leftOffset;
	private JTextField radiusText;
	private JTextField angleText;
	private JTextField distanceText;
	private JTextField rightOffset;
	private JTextArea debugText;
	private JButton btnClear;
	private MyRobot robot;
	private ThreadKeeper threadContainer;
//	private RobotLego robot;
	
	private boolean evitar,gestor,vaguear,segueparede;
	
//	private Thread evitarT,gestorT,vaguearT,segueparedeT;
	
	private VaguearT cVaguear;
	private AvoidObstacleThread cEvitar;
	private GestorThread cGestor;
	private SegueParede cSegue;
	
	private Semaphore acessoRobot;

	private String robotName;
	private boolean radioState;
	private boolean debugOnOff;
	private int rightOffsetValue;
	private int leftOffsetValue;
	private int distCtrl;
	private int radius;
	private int angle;
	private int distance;
	private JCheckBox chckbxFollow;
	private JTextField d_ctrlTextfield;
	
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	private void myInit() {
		//inicia as threads a null
//		this.evitarT = null;
//		this.vaguearT = null;
//		this.gestorT = null;
//		this.segueparedeT = null;
		
		this.threadContainer = new ThreadKeeper();
		
		//comportamentos a null------duvida, faz sentido?
		this.cVaguear = null;
		this.cEvitar = null;
		this.cGestor = null;
		this.cSegue = null;
		
		//semaforos a null
		this.acessoRobot = new Semaphore(0);
		
		//variaveis de controlo da checkboxes
		this.vaguear = false;
		this.evitar = false;
		this.gestor = false;
		this.segueparede = false;
		
		this.radioState = false;
		this.debugOnOff = false;
		this.radius = 0;
		this.angle = 0; 
		this.distance = 0;
		this.rightOffsetValue = 0;
		this.leftOffsetValue = 0;
		this.distCtrl = 0;
		this.robotName = "Nome do Robot";
		//para simula�oes True, para fisico False
		//this.robot = new MyRobot(false,this);
		this.robot = new MyRobot(true,this);
		//set ao sensor do robot
		this.robot.SetTouchSensor(RobotLego.S_2);
		this.robot.SetSensorLowSpeed(RobotLego.S_1);

		this.rdbtnOnoff.setSelected(this.radioState);
		this.chckbxDebug.setSelected(this.debugOnOff);
		this.chckbxWander.setSelected(this.vaguear);
		this.chckbxEvitar.setSelected(this.evitar);
		this.chckbxHandler.setSelected(this.gestor);
		this.robotNameText.setText(this.robotName);
	}
	
	private void launchThreads(){
		this.cVaguear = new VaguearT(this.robot,this.acessoRobot);
		this.cVaguear.start();
		this.cEvitar = new AvoidObstacleThread(this.robot,this.acessoRobot);
		this.cEvitar.start();
		this.cSegue = new SegueParede(this.robot,this.acessoRobot);
		this.cSegue.start();
		
		this.threadContainer.addThread(this.cVaguear);
		this.threadContainer.addThread(this.cEvitar);
		this.threadContainer.addThread(this.cSegue);
		
		this.cGestor = new GestorThread(this.robot, this.threadContainer);
		this.cGestor.start();
		
		showMessages(this.log("lan�ou threads"));
	}
	

	private void connectToRobot() {

		if (this.radioState == false) {
			boolean auxEstado;
			auxEstado = this.robot.OpenNXT(this.robotName);
			if (auxEstado == false) {
				this.rdbtnOnoff.setSelected(false);
				showMessages("Erro ao abrir o Robot: " + this.robotName);
				this.radioState = false;
			} else {
				this.rdbtnOnoff.setSelected(true);
				showMessages("Robot ligado : " + this.robotName);
				this.radioState = true;
				launchThreads();
			}
		} else {
			this.robot.CloseNXT();
			this.radioState = false;
			this.rdbtnOnoff.setSelected(false);
			showMessages("Robot Desligado: " + this.robotName);
		}
	}
	
	

	private void showMessages(String message) {
		if (this.debugOnOff) {
			this.debugText.append(message + "\n");
		} else {
			this.debugText.append("");
		}
	}

	private void setDistance(String distance) {
		try {
			this.distance = Integer.parseInt(distance);
		} catch (Exception e) {
			showMessages("Erro seguinte: " + e.getMessage());
		}
	}

	private void setRadius(String radius) {
		try {
			this.radius = Integer.parseInt(radius);
		} catch (Exception e) {
			showMessages("Erro seguinte: " + e.getMessage());
		}
	}
	
	private void setDistCtrl(String distance){
		try{	
			this.distCtrl = Integer.parseInt(distance);
		} catch (Exception e) {
			showMessages("Erro seguinte: " + e.getMessage());
		}
	}

	private void setRightOffset(String offset) {
		try {
			this.rightOffsetValue = Integer.parseInt(offset);
		} catch (Exception e) {
			showMessages("Erro seguinte: " + e.getMessage());
		}
	}

	private void setLeftOffset(String offset) {
		try {
			this.leftOffsetValue = Integer.parseInt(offset);
		} catch (Exception e) {
			showMessages("Erro seguinte: " + e.getMessage());
		}
	}

	private void setAngle(String angle) {
		try {
			this.angle = Integer.parseInt(angle);
		} catch (Exception e) {
			showMessages("Erro seguinte: " + e.getMessage());
		}
	}

	private void setRobotName(String name) {
		try {
			this.robotName = name;
		} catch (Exception e) {
			showMessages("Erro seguinte: " + e.getMessage());
		}
	}

	private void clearLog() {
		this.debugText.setText("");
	}

	private void actionForward() {
		// TODO Auto-generated method stub
		try {
			this.robot.Reta(this.distance);
			this.robot.Parar(false);
			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			showMessages("Robot nao disponivel: " + e.getMessage());
		}
	}

	private void actionBackwards() {
		try {
			this.robot.Reta(-this.distance);
			this.robot.Parar(false);
			
		} catch (Exception e) {
			showMessages("Robot nao disponivel: " + e.getMessage());
		}
	}

	private void actionRight() {
		try {
			this.robot.CurvarDireita(this.radius, this.angle);
			this.robot.Parar(false);
			
		} catch (Exception e) {
			showMessages("Robot nao disponivel: " + e.getMessage());
		}
	}

	private void actionLeft() {
		//
//		this.cVaguear.myWait();
		try {
			this.robot.CurvarEsquerda(this.radius, this.angle);
			this.robot.Parar(false);
			
		} catch (Exception e) {
			showMessages("Robot nao disponivel: " + e.getMessage());
		}
	}

	private void actionStop() {
		// robot parar a TRUE-------------------------------------
		// parar tem prioridade sobre qualquer outro movimento
		// independetemente do que ele esteja a fazer
		// -------------------------------------------------------

		// robot parar a FALSE------------------------------------
		// para o robot apenas quando acaba a ac�ao a que esta designado
		// -------------------------------------------------------
		try {
			this.robot.Parar(true);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			showMessages("Robot nao disponivel: " + e.getMessage());
		}
	}

	private void steeringLeft() {
		this.robot.AjustarVME(this.leftOffsetValue);
	}

	private void steeringRight() {
		this.robot.AjustarVMD(this.rightOffsetValue);
	}

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					new RobotInterfaceThreads();

				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public RobotInterfaceThreads() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 522, 530);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		rightOffset = new JTextField();
		rightOffset.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				setRightOffset(rightOffset.getText());
				showMessages("rightOffset -> " + rightOffsetValue);
			}
		});
		rightOffset.setBounds(459, 11, 37, 20);
		contentPane.add(rightOffset);
		rightOffset.setColumns(10);

		leftOffset = new JTextField();
		leftOffset.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				setLeftOffset(leftOffset.getText());
				showMessages("Left offset -> " + leftOffsetValue);
			}
		});
		leftOffset.setColumns(10);
		leftOffset.setBounds(10, 11, 37, 20);
		contentPane.add(leftOffset);

		JLabel lblLeftOffset = new JLabel("Left Offset");
		lblLeftOffset.setBounds(57, 14, 70, 14);
		contentPane.add(lblLeftOffset);

		JLabel lblRightOffset = new JLabel("Right Offset");
		lblRightOffset.setBounds(382, 14, 70, 14);
		contentPane.add(lblRightOffset);

		robotNameText = new JTextField();
		robotNameText.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				setRobotName(robotNameText.getText());
				showMessages("Nome do robot -> " + robotName);
			}
		});
		robotNameText.setBounds(192, 45, 115, 20);
		contentPane.add(robotNameText);
		robotNameText.setColumns(10);

		JLabel lblRobot = new JLabel("Robot");
		lblRobot.setBounds(155, 48, 46, 14);
		contentPane.add(lblRobot);

		rdbtnOnoff = new JRadioButton("On/Off");
		rdbtnOnoff.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				connectToRobot();
			}
		});
		rdbtnOnoff.setBounds(313, 44, 109, 23);
		contentPane.add(rdbtnOnoff);

		JLabel lblRaio = new JLabel("Radius");
		lblRaio.setBounds(10, 77, 46, 14);
		contentPane.add(lblRaio);

		radiusText = new JTextField();
		radiusText.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				setRadius(radiusText.getText());
				showMessages("Radius -> " + radius);
			}
		});
		radiusText.setBounds(58, 74, 30, 20);
		contentPane.add(radiusText);
		radiusText.setColumns(10);

		JLabel lblCm = new JLabel("cm");
		lblCm.setBounds(98, 77, 46, 14);
		contentPane.add(lblCm);

		JLabel lblAngulo = new JLabel("Angle");
		lblAngulo.setBounds(170, 80, 46, 14);
		contentPane.add(lblAngulo);

		angleText = new JTextField();
		angleText.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				setAngle(angleText.getText());
				showMessages("Angle -> " + angle);
			}
		});
		angleText.setColumns(10);
		angleText.setBounds(226, 76, 30, 20);
		contentPane.add(angleText);

		JLabel lblGraus = new JLabel("graus");
		lblGraus.setBounds(261, 80, 46, 14);
		contentPane.add(lblGraus);

		JLabel lblDistancia = new JLabel("Distance");
		lblDistancia.setBounds(339, 80, 56, 14);
		contentPane.add(lblDistancia);

		distanceText = new JTextField();
		distanceText.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				setDistance(distanceText.getText());
				showMessages("Distance -> " + distance);
			}
		});
		distanceText.setColumns(10);
		distanceText.setBounds(410, 77, 30, 20);
		contentPane.add(distanceText);

		JLabel lblCm_1 = new JLabel("cm");
		lblCm_1.setBounds(450, 80, 46, 14);
		contentPane.add(lblCm_1);

		JButton btnNewButton = new JButton("Forward");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				steeringLeft();
				steeringRight();
				actionForward();
				showMessages("Forward -> " + distance + "cm.");
			}

		});
		btnNewButton.setBounds(205, 141, 89, 47);
		contentPane.add(btnNewButton);

		JButton btnStop = new JButton("Stop");
		btnStop.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				actionStop();
				showMessages("STOP!");
			}
		});
		btnStop.setBackground(Color.RED);
		btnStop.setForeground(Color.BLACK);
		btnStop.setBounds(205, 187, 89, 47);
		contentPane.add(btnStop);

		JButton btnRight = new JButton("Right");
		btnRight.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
//				cEvitar.doAction();
				steeringLeft();
				steeringRight();
				actionRight();
				showMessages("Right -> " + distance + "cm.");
			}
		});
		btnRight.setBounds(292, 187, 89, 47);
		contentPane.add(btnRight);

		JButton btnLeft = new JButton("Left");
		btnLeft.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				steeringLeft();
				steeringRight();
				actionLeft();
				showMessages("Left -> " + distance + "cm.");
			}
		});
		btnLeft.setBounds(118, 187, 89, 47);
		contentPane.add(btnLeft);

		JButton btnBackwards = new JButton("Backwards");
		btnBackwards.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				steeringLeft();
				steeringRight();
				actionBackwards();
				showMessages("Backwards -> " + distance + "cm.");
			}
		});
		btnBackwards.setBounds(205, 233, 89, 47);
		contentPane.add(btnBackwards);

		chckbxDebug = new JCheckBox("Debug");
		chckbxDebug.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				debugOnOff = !debugOnOff;
				if (debugOnOff) {
					showMessages("Debug Ativo!");
				}
			}
		});
		chckbxDebug.setBounds(30, 318, 81, 23);
		contentPane.add(chckbxDebug);

		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(131, 306, 353, 160);
		contentPane.add(scrollPane);

		debugText = new JTextArea();
		debugText.setForeground(Color.BLACK);
		scrollPane.setViewportView(debugText);

		btnClear = new JButton("Clear Log");
		btnClear.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				clearLog();
			}
		});
		btnClear.setBounds(22, 369, 89, 23);
		contentPane.add(btnClear);

		chckbxHandler = new JCheckBox("Handler");
		chckbxHandler.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				gestor = !gestor;
//				chckbxEvitar.setEnabled(!gestor);
//				chckbxWander.setEnabled(!gestor);
//				chckbxFollow.setEnabled(!gestor);
				cGestor.updateCheck(gestor);
			}
		});
		chckbxHandler.setBounds(30, 283, 97, 23);
		contentPane.add(chckbxHandler);

		chckbxEvitar = new JCheckBox("Avoid");
		chckbxEvitar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				evitar = !evitar;
//				chckbxHandler.setEnabled(!evitar);
//				chckbxWander.setEnabled(!evitar);
//				chckbxFollow.setEnabled(!evitar);
				cEvitar.updateCheck(evitar);
			}
		});
		chckbxEvitar.setBounds(30, 257, 97, 23);
		contentPane.add(chckbxEvitar);

		chckbxWander = new JCheckBox("Wander");
		chckbxWander.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				vaguear = !vaguear;
//				chckbxEvitar.setEnabled(!vaguear);
//				chckbxHandler.setEnabled(!vaguear);
//				chckbxFollow.setEnabled(!vaguear);
				cVaguear.updateCheck(vaguear);
			}
		});
		chckbxWander.setBounds(30, 233, 89, 23);
		contentPane.add(chckbxWander);
		
		chckbxFollow = new JCheckBox("Follow");
		chckbxFollow.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				segueparede = !segueparede;
//				chckbxEvitar.setEnabled(!segueparede);
//				chckbxHandler.setEnabled(!segueparede);
//				chckbxWander.setEnabled(!segueparede);
			}
		});
		chckbxFollow.setBounds(30, 211, 81, 23);
		contentPane.add(chckbxFollow);
		
		d_ctrlTextfield = new JTextField();
		d_ctrlTextfield.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				setDistCtrl(d_ctrlTextfield.getText());
				if(radioState){
//					cSegue.setDistanceCTRL(distCtrl);
				}
				showMessages("dist_ctrl -> " + distCtrl);
			}
		});
		d_ctrlTextfield.setBounds(57, 105, 31, 20);
		contentPane.add(d_ctrlTextfield);
		d_ctrlTextfield.setColumns(10);
		
		JLabel lblDctrl = new JLabel("d-ctrl");
		lblDctrl.setBounds(10, 108, 46, 14);
		contentPane.add(lblDctrl);
		
		JLabel lblCm_2 = new JLabel("cm");
		lblCm_2.setBounds(98, 108, 46, 14);
		contentPane.add(lblCm_2);

		this.setVisible(true);

		myInit();
	}
}

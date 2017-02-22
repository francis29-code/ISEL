import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.JLabel;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class GUIplayer extends JFrame implements ILogger {

	/**
	 * 
	 */

	private JPanel contentPane;
	private MyRobot robot;
	private boolean record,play,playinv;
	
	/**
	 * Launch the application.
	 */

	private void myInit() {
		
		this.record = false;
		this.play = false;
		this.playinv = false;
	}

	/**
	 * Create the frame.
	 */
	public GUIplayer(MyRobot robot) {
		this.robot = robot;
		setBounds(100, 100, 142, 221);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JButton btnRecord = new JButton("RECORD");
		btnRecord.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				if(!record){
					record = !record;
					robot.setRecord(record);
				}
			}
		});
		btnRecord.setBounds(20, 51, 89, 23);
		contentPane.add(btnRecord);
		
		JButton btnPlay = new JButton("PLAY");
		btnPlay.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if(!play){
					play = !play;
					robot.setPlay(play);
					
				}
			}
		});
		btnPlay.setBounds(20, 85, 89, 23);
		contentPane.add(btnPlay);
		
		JButton btnPlayInv = new JButton("PLAY INV");
		btnPlayInv.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if(!playinv){
					playinv = !playinv;
					robot.setPlayInv(playinv);
				}
			}
		});
		btnPlayInv.setBounds(20, 119, 89, 23);
		contentPane.add(btnPlayInv);
		
		JButton btnStop = new JButton("STOP");
		btnStop.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				if(record){
					record = !record;
					robot.setRecord(record);
					robot.stopRecord();
				}
				if(play){
					play = !play;
					robot.setPlay(play);
				}
				if(playinv){
					playinv = !playinv;
					robot.setPlayInv(playinv);
				}
			}
		});
		btnStop.setBounds(20, 148, 89, 23);
		contentPane.add(btnStop);
		
		JLabel lblPlayer = new JLabel("PLAYER");
		lblPlayer.setBounds(50, 11, 46, 14);
		contentPane.add(lblPlayer);
		myInit();
	}

	@Override
	public String log(String message, Object... args) {
		// TODO Auto-generated method stub
		return null;
	}
}

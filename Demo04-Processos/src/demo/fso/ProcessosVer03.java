package demo.fso;

import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;
import javax.swing.JCheckBox;
import javax.swing.JFileChooser;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class ProcessosVer03 extends JFrame {

	private static final long serialVersionUID = 1L;
	
	private final JFileChooser fileChooser = new JFileChooser();
	
	private JPanel contentPane;
	private JTextField textFieldProcessName;
	private JTextField textFieldProcessArguments;
	private JLabel lblProcessName;
	private JLabel lblProcessArguments;
	private JButton buttonStartProcess;
	private JCheckBox checkBoxWaitForProcess;
	private JCheckBox checkBoxWaitInPassiveMode;
	private JCheckBox checkBoxUseProcessBuilder;
	private JButton buttonBrowseProcessName;
	private JButton buttonAddArgument;
	private JScrollPane scrollPaneProcessArguments;
	private JTextArea textAreaProcessArguments;
	private JButton buttonCleanArguments;
	
	private void waitForProcessInPassiveMode(Process proc) throws InterruptedException {
		System.out.println( "Vai esperar em modo passivo..." );
		proc.waitFor();
	}
	
	private void waitForProcessInActiveMode(Process proc) throws InterruptedException {
		System.out.println( "Vai esperar em modo activo..." );
		
		while (  proc.isAlive() )
			;
	}

	private void startProcessWithProcessBuilder() {
		try {
			System.out.println( "Criação de processos com ProcessBuilder..." );
			
			String processName;
			
			processName = this.textFieldProcessName.getText();
			
			List<String> args;
			args = new ArrayList<>();
			
			args.add( processName );
			args.addAll( this.parseArguments() );
			
			ProcessBuilder pb;
			pb = new ProcessBuilder( args );
		
			Process p = null;
			p = pb.start();
		
			System.out.printf( "Processo %s em execução\n", processName );

			if ( this.checkBoxWaitForProcess.isSelected() ) {
				if ( this.checkBoxWaitInPassiveMode.isSelected() ) {
					this.waitForProcessInPassiveMode( p );
				}
				else {
					this.waitForProcessInActiveMode( p );
				}
				
				System.out.printf( "Processo %s terminou com o código %d.\n", processName, p.exitValue() );
			}
		}
		catch (Exception e) {
			System.err.println( e.getMessage() );
		} 	
	}
	
	private void startProcessWithRuntime() {
		try {
			System.out.println( "Criação de processos com Runtime..." );
			
			String processName;
			
			processName = this.textFieldProcessName.getText();
			
			List<String> args;
			args = new ArrayList<>();
			
			args.add( processName );
			args.addAll( this.parseArguments() );
			
			Runtime currentRuntime;
			currentRuntime = Runtime.getRuntime();
			
			String[] argsAsArray;
			argsAsArray = args.toArray( new String[0] );
			
			Process p = null;
			p = currentRuntime.exec( argsAsArray );

			System.out.printf( "Processo %s em execução\n", processName );

			if ( this.checkBoxWaitForProcess.isSelected() ) {
				if ( this.checkBoxWaitInPassiveMode.isSelected() ) {
					this.waitForProcessInPassiveMode( p );
				}
				else {
					this.waitForProcessInActiveMode( p );
				}
				
				System.out.printf( "Processo %s terminou com o código %d.\n", processName, p.exitValue() );
			}
		}
		catch (Exception e) {
			System.err.println( e.getMessage() );
		} 	
	}
	
	private void startProcess() {
		if ( this.checkBoxUseProcessBuilder.isSelected() ) {
			this.startProcessWithProcessBuilder();
		}
		else {
			this.startProcessWithRuntime();
		}
	}
	
	private void browseProcessName() {
		int returnVal = this.fileChooser.showOpenDialog( this );
		
		if (returnVal == JFileChooser.APPROVE_OPTION) {
            File file = this.fileChooser.getSelectedFile();
            this.textFieldProcessName.setText( file.getAbsolutePath() );
        }
	}
	
	private void addArgument() {
		String currentArgument;
		currentArgument = this.textFieldProcessArguments.getText();
		
		this.textAreaProcessArguments.append( currentArgument + "\n" );
	}
	
	private void cleanArguments() {
		this.textAreaProcessArguments.setText( "" );
	}
	
	private List<String> parseArguments() {
		List<String> args;
		args = new ArrayList<>();
		
		String rawArguments;
		rawArguments = this.textAreaProcessArguments.getText();
		
		String[] argumentsAsArray;
		argumentsAsArray = rawArguments.split( "\n" );
		
		for (String currentArgument : argumentsAsArray) {
			args.add( currentArgument );
		}
		
		return args;
	}
	
	private void myInit() {
	}
	
	/**
	 * Create the frame.
	 */
	public ProcessosVer03() {
		setTitle("Processos - Vers\u00E3o 3");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 609, 567);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lblProcessName = new JLabel("Process Name");
		lblProcessName.setFont(new Font("Tahoma", Font.BOLD, 16));
		lblProcessName.setBounds(12, 13, 567, 16);
		contentPane.add(lblProcessName);
		
		textFieldProcessName = new JTextField();
		textFieldProcessName.setFont(new Font("Tahoma", Font.BOLD, 16));
		textFieldProcessName.setText("notepad.exe");
		textFieldProcessName.setBounds(12, 42, 399, 22);
		contentPane.add(textFieldProcessName);
		textFieldProcessName.setColumns(10);
		
		buttonBrowseProcessName = new JButton("Browse");
		buttonBrowseProcessName.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				browseProcessName();
			}
		});
		buttonBrowseProcessName.setFont(new Font("Tahoma", Font.BOLD, 16));
		buttonBrowseProcessName.setBounds(423, 42, 156, 25);
		contentPane.add(buttonBrowseProcessName);
		
		lblProcessArguments = new JLabel("Process Arguments");
		lblProcessArguments.setFont(new Font("Tahoma", Font.BOLD, 16));
		lblProcessArguments.setBounds(12, 77, 567, 16);
		contentPane.add(lblProcessArguments);
		
		textFieldProcessArguments = new JTextField();
		textFieldProcessArguments.setText("..\\goTrab01.bat");
		textFieldProcessArguments.setFont(new Font("Tahoma", Font.BOLD, 16));
		textFieldProcessArguments.setBounds(12, 106, 567, 22);
		contentPane.add(textFieldProcessArguments);
		textFieldProcessArguments.setColumns(10);
		
		buttonStartProcess = new JButton("Start Process");
		buttonStartProcess.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				startProcess();
			}
		});
		
		buttonAddArgument = new JButton("Add Argument");
		buttonAddArgument.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				addArgument();
			}
		});
		buttonAddArgument.setFont(new Font("Tahoma", Font.BOLD, 16));
		buttonAddArgument.setBounds(12, 141, 270, 25);
		contentPane.add(buttonAddArgument);
		
		buttonCleanArguments = new JButton("Clean Arguments");
		buttonCleanArguments.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				cleanArguments();
			}
		});
		buttonCleanArguments.setFont(new Font("Tahoma", Font.BOLD, 16));
		buttonCleanArguments.setBounds(309, 141, 270, 25);
		contentPane.add(buttonCleanArguments);
		
		scrollPaneProcessArguments = new JScrollPane();
		scrollPaneProcessArguments.setBounds(12, 179, 567, 200);
		contentPane.add(scrollPaneProcessArguments);
		
		textAreaProcessArguments = new JTextArea();
		textAreaProcessArguments.setFont(new Font("Monospaced", Font.BOLD, 16));
		scrollPaneProcessArguments.setViewportView(textAreaProcessArguments);
		buttonStartProcess.setFont(new Font("Tahoma", Font.BOLD, 16));
		buttonStartProcess.setBounds(12, 392, 567, 25);
		contentPane.add(buttonStartProcess);
		
		checkBoxWaitForProcess = new JCheckBox("Wait for Process");
		checkBoxWaitForProcess.setSelected(true);
		checkBoxWaitForProcess.setFont(new Font("Tahoma", Font.BOLD, 16));
		checkBoxWaitForProcess.setBounds(12, 426, 567, 25);
		contentPane.add(checkBoxWaitForProcess);
		
		checkBoxWaitInPassiveMode = new JCheckBox("Wait in Passive Mode");
		checkBoxWaitInPassiveMode.setSelected(true);
		checkBoxWaitInPassiveMode.setFont(new Font("Tahoma", Font.BOLD, 16));
		checkBoxWaitInPassiveMode.setBounds(12, 456, 567, 25);
		contentPane.add(checkBoxWaitInPassiveMode);
		
		checkBoxUseProcessBuilder = new JCheckBox("Use Process Builder");
		checkBoxUseProcessBuilder.setSelected(true);
		checkBoxUseProcessBuilder.setFont(new Font("Tahoma", Font.BOLD, 16));
		checkBoxUseProcessBuilder.setBounds(12, 486, 567, 25);
		contentPane.add(checkBoxUseProcessBuilder);
		
		myInit();
	}
}

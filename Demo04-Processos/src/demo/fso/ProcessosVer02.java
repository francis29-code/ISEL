package demo.fso;

import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;
import javax.swing.JCheckBox;

public class ProcessosVer02 extends JFrame {

	private static final long serialVersionUID = 1L;
	
	private JPanel contentPane;
	private JTextField textFieldProcessName;
	private JTextField textFieldProcessArguments;
	private JLabel lblProcessName;
	private JLabel lblProcessArguments;
	private JButton buttonStartProcess;
	private JCheckBox checkBoxWaitForProcess;
	private JCheckBox checkBoxWaitInPassiveMode;
	private JCheckBox checkBoxUseProcessBuilder;
	
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
			
			String processName, processArguments;
			
			processName = this.textFieldProcessName.getText();
			processArguments = this.textFieldProcessArguments.getText();
			
			List<String> args;
			args = new ArrayList<>();
			
			args.add( processName );
			args.add( processArguments );
			
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
			
			String processName, processArguments;
			
			processName = this.textFieldProcessName.getText();
			processArguments = this.textFieldProcessArguments.getText();
			
			List<String> args;
			args = new ArrayList<>();
			
			args.add( processName );
			args.add( processArguments );
			
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
	
	/**
	 * Create the frame.
	 */
	public ProcessosVer02() {
		setTitle("Processos - Vers\u00E3o 2");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 412);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lblProcessName = new JLabel("Process Name");
		lblProcessName.setFont(new Font("Tahoma", Font.BOLD, 16));
		lblProcessName.setBounds(12, 13, 408, 16);
		contentPane.add(lblProcessName);
		
		textFieldProcessName = new JTextField();
		textFieldProcessName.setFont(new Font("Tahoma", Font.BOLD, 16));
		textFieldProcessName.setText("notepad.exe");
		textFieldProcessName.setBounds(12, 42, 408, 22);
		contentPane.add(textFieldProcessName);
		textFieldProcessName.setColumns(10);
		
		lblProcessArguments = new JLabel("Process Arguments");
		lblProcessArguments.setFont(new Font("Tahoma", Font.BOLD, 16));
		lblProcessArguments.setBounds(12, 77, 408, 16);
		contentPane.add(lblProcessArguments);
		
		textFieldProcessArguments = new JTextField();
		textFieldProcessArguments.setText("..\\goTrab01.bat");
		textFieldProcessArguments.setFont(new Font("Tahoma", Font.BOLD, 16));
		textFieldProcessArguments.setBounds(12, 106, 408, 22);
		contentPane.add(textFieldProcessArguments);
		textFieldProcessArguments.setColumns(10);
		
		buttonStartProcess = new JButton("Start Process");
		buttonStartProcess.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				startProcess();
			}
		});
		buttonStartProcess.setFont(new Font("Tahoma", Font.BOLD, 16));
		buttonStartProcess.setBounds(12, 140, 408, 25);
		contentPane.add(buttonStartProcess);
		
		checkBoxWaitForProcess = new JCheckBox("Wait for Process");
		checkBoxWaitForProcess.setSelected(true);
		checkBoxWaitForProcess.setFont(new Font("Tahoma", Font.BOLD, 16));
		checkBoxWaitForProcess.setBounds(12, 174, 408, 25);
		contentPane.add(checkBoxWaitForProcess);
		
		checkBoxWaitInPassiveMode = new JCheckBox("Wait in Passive Mode");
		checkBoxWaitInPassiveMode.setSelected(true);
		checkBoxWaitInPassiveMode.setFont(new Font("Tahoma", Font.BOLD, 16));
		checkBoxWaitInPassiveMode.setBounds(12, 204, 408, 25);
		contentPane.add(checkBoxWaitInPassiveMode);
		
		checkBoxUseProcessBuilder = new JCheckBox("Use Process Builder");
		checkBoxUseProcessBuilder.setSelected(true);
		checkBoxUseProcessBuilder.setFont(new Font("Tahoma", Font.BOLD, 16));
		checkBoxUseProcessBuilder.setBounds(12, 234, 408, 25);
		contentPane.add(checkBoxUseProcessBuilder);
	}
}

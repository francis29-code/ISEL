package demo.fso;

import java.awt.EventQueue;

public class ProcessosLauncherVer02 {

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ProcessosVer02 frame = new ProcessosVer02();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

}

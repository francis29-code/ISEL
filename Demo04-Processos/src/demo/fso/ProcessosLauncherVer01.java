package demo.fso;

import java.awt.EventQueue;

public class ProcessosLauncherVer01 {

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ProcessosVer01 frame = new ProcessosVer01();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

}

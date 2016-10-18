package demo.fso;

import java.awt.EventQueue;

public class ProcessosLauncherVer03 {

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					ProcessosVer03 frame = new ProcessosVer03();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

}

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class GestorThread {

	// tempo de espera para ler o proprio ficheiro
	private static final int SLEEP_TIME = 1000;
	// caixas de correio para cada processo
	private int estado;
	static private final int init = 0;
	static private final int vaguear = 1;
	static private final int avoid = 2;
	static private final int closeVaguear = 3;
	static private final int closeAvoid = 4;
	static private final int Terminar = 5;

	public GestorThread() {
		this.estado = init;

	}

	public void launchProcesses() {

		while (estado != Terminar) {
			switch (estado) {
			case init:
				System.out.println("estado: init");
				

			case vaguear:
				System.out.println("estado vaguear");
				
				
			case avoid:
				System.out.println("estado avoid");
				
			}

		}

	}
	
	
	public static void main(String []args){
		GestorThread ge;
		ge = new GestorThread();
		ge.launchProcesses();
	}

}

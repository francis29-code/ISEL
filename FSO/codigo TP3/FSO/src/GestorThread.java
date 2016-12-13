import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class GestorThread {

	// tempo de espera para ler o proprio ficheiro
	private static final int SLEEP_TIME = 1000;
	// caixas de correio para cada processo
	
	public enum States {Vaguear, Evitar, SegueParede, Terminar, Init};
	private States estado;

	public GestorThread(VaguearT vaguear, AvoidObstacleThread avoid) {
		this.estado = States.Init;

	}

	public void launchProcesses() {

		while (this.estado != States.Terminar) {
			switch (this.estado) {
			case Init:
				System.out.println("estado: init");
				

			case Vaguear:
				System.out.println("estado vaguear");
				
				
			case Evitar:
				System.out.println("estado avoid");
				
			default:
				break;
				
			}

		}

	}

}

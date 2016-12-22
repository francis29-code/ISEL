import java.util.concurrent.Semaphore;

public class AvoidObstacleThread extends Thread implements ILogger {
	final int MAX_DISTANCE = 15;

	final int MAX_ANGLE = 90;

	final int MAX_RADIUS = 0;

	protected String robotName;

	protected MyRobot theRobot;

	private Semaphore semaphore;

	private boolean hit;

	public enum States {
		Running, Waiting, Ending, Reading
	};

	private States currentState;

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public AvoidObstacleThread(MyRobot robot, Semaphore semaphore) {
		this.currentState = States.Waiting;
		this.theRobot = robot;
		this.semaphore = semaphore;
		this.hit = false;
		this.setName("evitar");
	}

	public boolean readSensor() {
		boolean aux = this.theRobot.GetTouchSensor();
		if(!aux){
			return false;
		}
		else{
			return true;
		}
		 
	}

	public boolean hit() {
		return this.hit;
	}

	public void resetHit() {
		this.hit = false;
	}

	@Override
	public void run() {
		while (this.currentState != States.Ending) {

			switch (this.currentState) {
			case Waiting:
				//estado inicial quando se liga o robot na interface grafica
				myWaiting();
				break;
			case Reading:
				myReading();
				break;

			case Running:
				myAction();
				break;
			default:
				break;
			}

		}
	}

	private void myWaiting() {
//		try {
//			// fica bloqueado sem fazer acção nenhuma
//			// até que a sua maquina de estados sofra alterações
//			// this.log("ANTES DO SEMAFORO EVITAR");
//			this.semaphore.acquire();
//			// this.log("DEPOIS DO SEMAFORO EVITAR");
//		} catch (InterruptedException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
	}

	private void myAction() {
		try {
			this.semaphore.acquire();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.theRobot.Reta(-MAX_DISTANCE);
		this.theRobot.CurvarEsquerda(MAX_RADIUS, MAX_ANGLE);
		this.theRobot.Parar(false);
		this.currentState = States.Reading;
	}

	private void myReading() {
		// this.log("---------------------esperando no
		// EVITAR---------------------");
		if (readSensor()) {
			this.log("SENSOR A TRUE----------------------------------------------------------------");
			this.theRobot.Parar(true);
			this.hit = true;
		}
		
		try {
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	public void myStart() {
		this.currentState = States.Reading;
	}

	public void myPause() {
		// pausa o trabalho do vaguear, sem terminar o ciclo
		this.currentState = States.Waiting;
		// this.log("---------------------pausei no
		// EVITAR---------------------");

	}

	public void myResume() {
		// inicia o comportamento do vaguear
		this.currentState = States.Running;
		this.semaphore.release();
		// this.log("---------------------estou a correr no
		// EVITAR---------------------");
	}

	public void myEnding() {
		// encerra o trabalho da thread
		this.currentState = States.Ending;
		// this.log("---------------------estou acabar o
		// EVITAR---------------------");
	}

}

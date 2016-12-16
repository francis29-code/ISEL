import java.util.Random;
import java.util.concurrent.Semaphore;

public class VaguearT extends Thread implements ILogger {
	public final int MinForward = 50; // Centimeters
	public final int RndForward = 40; // Centimeters

	public final int MinRadius = 50; // Centimeters
	public final int RndRadius = 30; // Centimeters

	public final int MinAngle = 30; // Degrees
	public final int RndAngle = 60; // Degrees

	public final int SensorSleepTime = 250; // Milliseconds

	public enum Directions {
		Stop, Right, Left, Forward
	};

	public enum States {
		Running, Waiting, Ending
	};

	public Directions currentDirection;

	public States currentState;

	protected String robotName;

	protected Random rnd;

	protected RobotLego theRobot;

	private Semaphore semaphore;

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public VaguearT(RobotLego robot, Semaphore semaphore) {
		this.currentDirection = Directions.Stop;
		this.theRobot = robot;
		this.semaphore = semaphore;
		this.currentState = States.Waiting;
		this.rnd = new Random();
	}

	private Directions getNextDirection() {
		int aux;
		aux = this.rnd.nextInt(90);

		if (aux < 30) {
			return Directions.Right;
		}

		if (aux < 60) {
			return Directions.Left;
		}

		return Directions.Forward;
	}

	private int getRandomRadius() {
		return this.MinRadius + this.rnd.nextInt(this.RndRadius);
	}

	private int getRandomAngle() {
		return this.MinAngle + this.rnd.nextInt(this.RndAngle);
	}

	private int getRandomDistance() {
		return this.MinForward + this.rnd.nextInt(this.RndForward);
	}

	private double getCurveDistance(double angle, double radius) {
		double perimeter = 2.0 * Math.PI * radius;
		return angle * perimeter / 360.0;
	}

	private double getSleepTime(double distance) {
		double sleepTime;
		sleepTime = distance * 5.0 / 100.0;

		this.log("getSleepTime(%3.2f)->%3.2f", distance, sleepTime);

		return sleepTime;
	}

	private double getSleepTime(double angle, double radius) {
		return getSleepTime(getCurveDistance(angle, radius));
	}

	public void doWork() throws Exception {

		double radius, angle, distance;

		double sleepTime = 0.0;

		for (; this.currentState == States.Running;) {
			Directions newDirection;

			while ((newDirection = getNextDirection()) == this.currentDirection)
				;

			this.currentDirection = newDirection;

			switch (this.currentDirection) {
			case Right:
				radius = getRandomRadius();
				angle = getRandomAngle();
				sleepTime = getSleepTime(angle, radius);
				this.theRobot.CurvarDireita((int) radius, (int) angle);
				this.log("Right(%3.2f, %3.2f)->%3.2f", radius, angle, getCurveDistance(radius, angle));

				break;
			case Forward:
				distance = getRandomDistance();
				sleepTime = getSleepTime(distance);
				this.theRobot.Reta((int) distance);
				this.log("Forward(%3.2f)", distance);
				break;
			case Left:
				radius = getRandomRadius();
				angle = getRandomAngle();
				sleepTime = getSleepTime(angle, radius);
				this.theRobot.CurvarEsquerda((int) radius, (int) angle);
				this.log("Left(%3.2f, %3.2f)->%3.2f", radius, angle, getCurveDistance(radius, angle));
				break;
			default:
				break;
			}
			// Uncomment next line to force a stop after each movement
			// this.theRobot.Parar( false );
			Thread.sleep((int) (sleepTime * 1000.0));
			this.log("Sleep(%3.2f)", sleepTime);
			/// falta fazer check ao semaforo para parar o CICLO DO VAGUEAR WORK
			/// = FALSE

			// this.theRobot.CloseNXT();
		}
	}

	public void myWait() {
		// fica bloqueado sem fazer acção nenhuma
		// até que a sua maquina de estados sofra alterações
//		try {
//
//			this.semaphore.acquire();
//			// this.log("---------------------estou a espera no
//			// VAGUEAR---------------------");
//		} catch (InterruptedException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
		// experimentar com gestor se funciona
		// this.semaphore.release();
	}

	public void myPause() {
		// pausa o trabalho do vaguear, sem terminar o ciclo
		this.currentState = States.Waiting;
		// this.log("---------------------pausei no
		// VAGUEAR---------------------");
	}

	public void myResume() {
		// inicia o comportamento do vaguear
		this.currentState = States.Running;
		this.semaphore.release();
		// this.log("---------------------estou a correr no
		// VAGUEAR---------------------");
	}

	public void myEnding() {
		// encerra o trabalho da thread
		this.currentState = States.Ending;
		// this.log("---------------------estou acabar o
		// VAGUEAR---------------------");
	}

	@Override
	public void run() {
		while (this.currentState != States.Ending) {
			switch (this.currentState) {
			case Waiting:
				myWait();
				break;

			case Running:
				try {
					this.semaphore.acquire();
					doWork();
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			default:
				break;
			}

		}

	}

}

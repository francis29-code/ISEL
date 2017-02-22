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

	public Directions currentDirection;

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

	public void doWork() throws Exception {
		boolean work;
		work = true;

		double radius, angle, distance;

		double sleepTime = 0.0;

		for (; work == true;) {
			Directions newDirection;

			while ((newDirection = getNextDirection()) == this.currentDirection)
				;

			this.currentDirection = newDirection;

			switch (this.currentDirection) {
			case Right:
				radius = getRandomRadius();
				angle = getRandomAngle();
				this.theRobot.CurvarDireita((int) radius, (int) angle);
				this.log("Right(%3.2f, %3.2f)->%3.2f", radius, angle, getCurveDistance(radius, angle));

				break;
			case Forward:
				distance = getRandomDistance();
				this.theRobot.Reta((int) distance);
				this.log("Forward(%3.2f)", distance);
				break;
			case Left:
				radius = getRandomRadius();
				angle = getRandomAngle();
				this.theRobot.CurvarEsquerda((int) radius, (int) angle);
				this.log("Left(%3.2f, %3.2f)->%3.2f", radius, angle, getCurveDistance(radius, angle));
				break;
			default:
				break;
			}
			// Uncomment next line to force a stop after each movement
			// this.theRobot.Parar( false );

			this.log("Sleep(%3.2f)", sleepTime);
			///falta fazer check ao semaforo para parar o CICLO DO VAGUEAR WORK = FALSE

//			this.theRobot.CloseNXT();
		}
	}
	
	@Override
	public void run(){
		//automato principal na espera do semaphore
		//acquire atraves de um booleano
		//release
	}

	public static void main(String[] args) {

		VaguearT v;
		v = new VaguearT(new RobotLego(), new Semaphore(1));

	}

}

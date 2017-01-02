import java.util.Random;
import java.util.concurrent.Semaphore;


public class VaguearT extends Thread implements ILogger {
	public final int MinForward = 50; // Centimeters
	public final int RndForward = 40; // Centimeters

	public final int MinRadius = 50; // Centimeters
	public final int RndRadius = 30; // Centimeters

	public final int MinAngle = 30; // Degrees
	public final int RndAngle = 60; // Degrees

	final static int SLEEP_TIME_SENSOR = 1000;

	public enum Directions {
		Stop, Right, Left, Forward
	};

	public Directions currentDirection;

	public States currentState;

	protected String robotName;

	protected Random rnd;

	protected MyRobot theRobot;
	
	private boolean checked;

	private Semaphore semaphore;
	
	private int currentSleep;

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public VaguearT(MyRobot robot, Semaphore semaphore) {
		
		this.setName("Vaguear");
		
		this.currentDirection = Directions.Stop;
		this.theRobot = robot;
		this.semaphore = semaphore;
		this.currentState = States.Waiting;
		this.rnd = new Random();
		this.checked = false;
	}
	
	public States currentState(){
		return this.currentState;
	}
	
	public boolean isChecked(){
		return this.checked;
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
				setSleepTime((int)sleepTime);
				this.theRobot.CurvarDireita((int) radius, (int) angle);
				this.log("Right(%3.2f, %3.2f)->%3.2f", radius, angle, getCurveDistance(radius, angle));

				break;
			case Forward:
				distance = getRandomDistance();
				sleepTime = getSleepTime(distance);
				setSleepTime((int)sleepTime);
				this.theRobot.Reta((int) distance);
				this.log("Forward(%3.2f)", distance);
				break;
			case Left:
				radius = getRandomRadius();
				angle = getRandomAngle();
				sleepTime = getSleepTime(angle, radius);
				setSleepTime((int)sleepTime);
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

	@Override
	public synchronized void run() {
		while (this.currentState != States.Ending) {
			switch (this.currentState) {
			case Waiting:
				try {
					Thread.sleep(SLEEP_TIME_SENSOR);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				this.log("ESTOU NO WAITING VAGUEAR");
				if(this.checked){
					try {
						this.semaphore.acquire();
						this.currentState = States.Running;
					} catch (InterruptedException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				break;

			case Running:
				this.log("ESTOU NO RUNNING VAGUEAR");
				try {

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
	
	private void setSleepTime(int sleepTime){
		this.currentSleep = sleepTime;
	}
	
	public int getSleepTime(){
		return this.currentSleep;
	}
	
	public void updateCheck(boolean check){
		this.checked = check;
		if(!this.checked){
			this.currentState = States.Waiting;
			this.log("MANDEI PARA O WAITING");
		}
	}
	
	public void workPermission(){
		this.semaphore.release();
	}
	
	public void myPause(){
		this.currentState = States.Waiting;
	}
	
	

}

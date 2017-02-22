import java.util.concurrent.Semaphore;

public class AvoidObstacleThread extends Thread implements ILogger {
	final static int MAX_DISTANCE = 15;

	final static int MAX_ANGLE = 90;

	final static int MAX_RADIUS = 0;

	final static int SLEEP_TIME_SENSOR = 1000;

	protected String robotName;

	protected MyRobot theRobot;

	private Semaphore acessoRobot, ownSemaphore;

	private boolean checked;

	private States currentState;

	@Override
	public String log(String message, Object... args) {
		String aux1, aux2;
		aux1 = String.format( message, args );
		
		aux2 = String.format( "[%s] %s", this.getName(), aux1 );

		System.out.println( aux2 );

		return aux2;
	}

	public AvoidObstacleThread(MyRobot robot, Semaphore semaphore) {
		this.setName("Evitar");
		this.currentState = States.Waiting;
		this.theRobot = robot;
		this.ownSemaphore = new Semaphore(0);
		this.acessoRobot = semaphore;
		this.checked = false;
	}

	@Override
	public void run() {
		while (this.currentState != States.Ending) {
			switch (this.currentState) {
			case Waiting:
				this.log("ESTOU NO WAITING EVITAR");
				// estado à espera de uma alteração
				try {
					this.ownSemaphore.acquire();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}

				break;

			case Reading:
//				this.log("ESTOU NO READING EVITAR");
				doReading();
				break;

			case Running:
//				this.log("ESTOU NO RUNNING EVITAR");
				doAvoid();
				break;
			default:
				break;
			}
		}
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

	public States currentState() {
		return this.currentState;
	}

	private void doAvoid() {
		this.theRobot.Reta(-MAX_DISTANCE);
		try {
			Thread.sleep((int) (getSleepTime(MAX_DISTANCE) * 1000));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.theRobot.CurvarEsquerda(MAX_RADIUS, MAX_ANGLE);
		try {
			Thread.sleep((int) (getSleepTime(MAX_ANGLE, MAX_RADIUS) * 1000));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (this.currentState != States.Waiting) {
			this.currentState = States.Reading;
		}

		this.acessoRobot.release();
	}

	public int totalSleepTime() {

		double firstSleep = getSleepTime(MAX_DISTANCE);
		double secondSleep = getSleepTime(MAX_ANGLE, MAX_RADIUS);

		return (int) (firstSleep + secondSleep);
	}

	private void doReading() {
		if (this.theRobot.GetTouchSensor()) {
			try {
				this.theRobot.Parar(true);
				this.acessoRobot.acquire();
				
				if (this.currentState != States.Waiting) {
					this.currentState = States.Running;

				}
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		// menor o sleep mais rapida a resposta
		try {
			// 1000 ms para robot virtual
			// 100 para robot fisico
			Thread.sleep(100);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public void myReading() {
		this.ownSemaphore.release();
		this.currentState = States.Reading;
	}

	public void myPause() {
		this.currentState = States.Waiting;
	}

	public void updateCheck(boolean checkbox) {
		this.checked = checkbox;
		if (!this.checked) {
			myPause();
			this.log("MANDEI PARA O WAITING");
		} else {
			myReading();
		}
	}

}

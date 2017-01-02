import java.util.concurrent.Semaphore;

public class AvoidObstacleThread extends Thread implements ILogger {
	final static int MAX_DISTANCE = 15;

	final static int MAX_ANGLE = 90;

	final static int MAX_RADIUS = 0;
	
	final static int SLEEP_TIME_SENSOR = 1000;

	protected String robotName;

	protected MyRobot theRobot;

	private Semaphore semaphore;

	private boolean contact, checked;

	private States currentState;

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public AvoidObstacleThread(MyRobot robot, Semaphore semaphore) {
		this.setName("Evitar");
		this.currentState = States.Waiting;
		this.theRobot = robot;
		this.contact = false;
		this.semaphore = semaphore;
		this.checked = false;
	}


	@Override
	public void run() {
		while(this.currentState != States.Ending){
			switch(this.currentState){
			case Waiting:
				this.log("ESTOU NO WAITING EVITAR");
				//estado à espera de uma alteração
				try {
					Thread.sleep(SLEEP_TIME_SENSOR);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				if(this.checked){
					this.currentState = States.Reading;
				}
		
				break;
				
			case Reading:
				this.log("ESTOU NO READING EVITAR");
				doReading();
				break;
				
			case Running:
				this.log("ESTOU NO RUNNING EVITAR");
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
	
	public States currentState(){
		return this.currentState;
	}
	
	private void doAvoid(){
		try {
			this.semaphore.acquire();
		} catch (InterruptedException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		this.theRobot.Reta(-MAX_DISTANCE);
		try {
			Thread.sleep((int)(getSleepTime(MAX_DISTANCE)*1000));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		this.theRobot.CurvarEsquerda(MAX_RADIUS, MAX_ANGLE);
		try {
			Thread.sleep((int)(getSleepTime(MAX_ANGLE, MAX_RADIUS)*1000));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		resetContact();
		this.currentState = States.Reading;
	}
	
	public int totalSleepTime(){
		
		double firstSleep = getSleepTime(MAX_DISTANCE);
		double secondSleep = getSleepTime(MAX_ANGLE, MAX_RADIUS);
		
		return (int)(firstSleep + secondSleep);
	}
	
	private void doReading(){
		if(this.theRobot.GetTouchSensor()){
			this.theRobot.Parar(true);
			this.contact = true;
//			this.semaphore.release();
			this.currentState = States.Running;
		}
		try {
			Thread.sleep(SLEEP_TIME_SENSOR);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public boolean hadContact(){
		return this.contact;
	}
	
	public void resetContact(){
		this.contact = false;
	}

	public void doAction(){
		this.semaphore.release();
	}
	
	
	public void updateCheck(boolean checkbox){
		this.checked = checkbox;
		if(!this.checked){
			this.currentState = States.Waiting;
			this.log("MANDEI PARA O WAITING");
		}
	}



}

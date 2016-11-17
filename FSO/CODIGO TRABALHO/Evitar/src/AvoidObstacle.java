
public class AvoidObstacle implements ILogger {
	final int MAX_DISTANCE = 15;

	final int MAX_ANGLE = 90;

	final int MAX_RADIUS = 0;

	protected String robotName;

	protected MyRobot theRobot;
	
	private MailBoxGestor mailEvitar;
	private MailBoxGestor mailGestor;
	private String prefix = "PA ";
	


	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public AvoidObstacle(String name, int sensor, boolean simulateRobot) {
		this.robotName = name;
		
		//Cada classe lê o seu proprio mail mas escreve no mail do destinatário
		
		this.mailEvitar = new MailBoxGestor("evitar.dat");
		this.mailGestor = new MailBoxGestor("gestor.dat");
		
		
		
		this.theRobot = new MyRobot(simulateRobot, this);

		if (this.theRobot.OpenNXT(this.robotName) == false) {
			String message;
			message = this.log("Could not connect to robot %s", this.robotName);

			throw new IllegalArgumentException(message);
		}

		this.theRobot.SetSpeed(50);
		this.theRobot.SetTouchSensor(sensor);

	}

	public boolean readSensor() {
		return this.theRobot.GetTouchSensor() == true;
	}

	public void doAvoidObstacle() {
		double sleep = 0.;
		while(readSensor()) {
			try {
				this.theRobot.Reta(-MAX_DISTANCE);
				// this.log("backwards(%3.2d)", MAX_DISTANCE);
				this.theRobot.CurvarEsquerda(MAX_RADIUS, MAX_ANGLE);
				// this.log("Right(%3.2d, %3.2d)->%3.2d", MAX_RADIUS, MAX_ANGLE,
				sleep = getSleepTime(MAX_RADIUS, MAX_ANGLE)+getSleepTime(MAX_DISTANCE);
				Thread.sleep((long)sleep);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			this.theRobot.Parar(true);
		}
		this.theRobot.CloseNXT();
		this.mailGestor.write(prefix +"stop");
		readMailBox();
	}
	
	public void readMailBox(){
		while(mailEvitar.read() != "exe"){
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		doAvoidObstacle();
	}
	private double getCurveDistance(double angle, double radius) {
		double perimeter = 2.0 * Math.PI * radius;
		return angle * perimeter / 360.0;
	}
	private double getSleepTime(double distance) {
		double sleepTime;
		sleepTime = distance * 5.0 / 100.0;
		
		this.log( "getSleepTime(%3.2f)->%3.2f", distance, sleepTime);
		
		return sleepTime;
	}
	private double getSleepTime(double angle, double radius) { 
		return getSleepTime ( getCurveDistance(angle, radius) );
	}
	
	

}

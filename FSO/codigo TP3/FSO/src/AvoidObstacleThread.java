import java.util.concurrent.Semaphore;

public class AvoidObstacleThread implements ILogger {
	final int MAX_DISTANCE = 15;

	final int MAX_ANGLE = 90;

	final int MAX_RADIUS = 0;

	protected String robotName;

	protected RobotLego theRobot;
	
	private Semaphore semaphore;

	

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public AvoidObstacleThread(RobotLego robot, Semaphore semaphore) {

		this.theRobot = robot;
		this.semaphore = semaphore;

	}


	public void doAvoidObstacle() {

		// double sleep = 0.;
		//corrigir automato para ler o sensor
//		while (readSensor()) {
//			try {
//				this.theRobot.Reta(-MAX_DISTANCE);//				// this.log("backwards(%3.2d)", MAX_DISTANCE);
//				this.theRobot.CurvarEsquerda(MAX_RADIUS, MAX_ANGLE);
//				// this.log("Right(%3.2d, %3.2d)->%3.2d", MAX_RADIUS, MAX_ANGLE,
//				// sleep = getSleepTime(MAX_RADIUS,
//				// MAX_ANGLE)+getSleepTime(MAX_DISTANCE);
//
//				Thread.sleep(600);
//				// Thread.sleep(1000);
//			} catch (InterruptedException e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			}
//			this.theRobot.Parar(true);
//		}
		this.theRobot.CloseNXT();

	}


	public static void main(String[] args) {
		RobotLego robot;
		robot = new RobotLego();
		AvoidObstacleThread ao;
		ao = new AvoidObstacleThread(robot, new Semaphore(1));


	}

}

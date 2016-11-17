
public class AvoidObstacle implements ILogger {
	final int MAX_DISTANCE = 15;

	final int MAX_ANGLE = 90;

	final int MAX_RADIUS = 0;

	protected String robotName;

	protected MyRobot theRobot;
	
	private MailBox mailEvitar;
	private MailBox mailGestor;


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
		
		this.mailEvitar = new MailBox("evitar.dat");
		this.mailGestor = new MailBox("gestor.dat");
		
		
		
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

		while(readSensor()) {
			this.theRobot.Reta(-MAX_DISTANCE);
			// this.log("backwards(%3.2d)", MAX_DISTANCE);
			this.theRobot.CurvarEsquerda(MAX_RADIUS, MAX_ANGLE);
			// this.log("Right(%3.2d, %3.2d)->%3.2d", MAX_RADIUS, MAX_ANGLE,
			// getCurveDistance(MAX_RADIUS, MAX_ANGLE) );
			this.theRobot.Parar(false);
		}
		this.theRobot.CloseNXT();
		this.mailGestor.write("stop");
		readMailBox();
	}
	
	public void readMailBox(){
		while(mailEvitar.read() != "exe"){
			try {
				Thread.sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		doAvoidObstacle();
	}
	
	

}

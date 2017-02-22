import com.sun.webkit.dom.DOMWindowImpl;

public class AvoidObstacle implements ILogger {
	final int MAX_DISTANCE = 15;

	final int MAX_ANGLE = 90;

	final int MAX_RADIUS = 0;

	protected String robotName;

	protected MyRobot theRobot;

	private MailBox mailEvitar;
	private MailBox mailGestor;
	private MailBox mailGUI;
	private String prefixAvoid = "PA";
	private String prefixGestor = "PG";
	private String prefixGUI = "PGUI";
	private boolean guiorgestor;
	private boolean simulate;
	private int sensor;

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public AvoidObstacle(String name, int sensor, boolean simulateRobot, boolean guiorgestor) {
		this.robotName = name;
		this.guiorgestor = guiorgestor;
		this.simulate = simulateRobot;
		this.sensor = sensor;
		// Cada classe lê o seu proprio mail mas escreve no mail do destinatário

		this.mailEvitar = new MailBox("evitar.dat");
		this.mailGestor = new MailBox("gestor.dat");
		this.mailGUI = new MailBox("gui.dat");

		if (!this.guiorgestor) {
			this.theRobot = new MyRobot(simulateRobot, this);

			if (this.theRobot.OpenNXT(this.robotName) == false) {
				String message;
				message = this.log("Could not connect to robot %s", this.robotName);

				throw new IllegalArgumentException(message);
			}

			this.theRobot.SetSpeed(50);
			this.theRobot.SetTouchSensor(sensor);
		}

	}

	public boolean readSensor() {
		return this.theRobot.GetTouchSensor() == true;
	}

	public void doAvoidObstacle() {

		while (readSensor()) {
			try {
				this.theRobot.Reta(-MAX_DISTANCE);
				this.theRobot.CurvarEsquerda(MAX_RADIUS, MAX_ANGLE);
				Thread.sleep(600);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			this.theRobot.Parar(true);
		}
		this.theRobot.CloseNXT();
		if (!this.guiorgestor) {
			this.mailGestor.write(prefixAvoid + "sstop");
		}else{
			this.mailGUI.write(prefixAvoid + "sstop");
		}
		readMailBox();
	}

	public void readMailBox() {
		while (!mailEvitar.read().startsWith(prefixGestor)) {
			try {

				Thread.sleep(600);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		try {
			this.log("verifica content PEVITAR:------------------- " + this.mailEvitar.read());
			if(mailEvitar.read().contains("PGUIstart")){
				this.log("ENTREI NO PGUIStart");
				//consome
				this.mailEvitar.eraseContent();
				this.theRobot = new MyRobot(simulate, this);

				if (this.theRobot.OpenNXT(this.robotName) == false) {
					String message;
					message = this.log("Could not connect to robot %s", this.robotName);

					throw new IllegalArgumentException(message);
				}
				this.theRobot.SetSpeed(50);
				this.theRobot.SetTouchSensor(sensor);
				doAvoidObstacle();
			}
			else if (mailEvitar.read().contains("PGstart")) {
				// tem de consumir
				this.mailEvitar.eraseContent();
				doAvoidObstacle();
			} else if (mailEvitar.read().contains("sstop")) {
				this.mailEvitar.eraseContent();
				this.mailEvitar.closeChannel();
				this.theRobot.Parar(true);
				this.theRobot.CloseNXT();
			}

		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public static void main(String[] args) {
		String nome;
		int port;
		boolean simulate;
		boolean guiorgestor;

		nome = args[0];
		port = Integer.parseInt(args[1]);
		simulate = Boolean.parseBoolean(args[2]);
		guiorgestor = Boolean.parseBoolean(args[3]);
		AvoidObstacle ao;
		ao = new AvoidObstacle(nome, port, simulate, guiorgestor);
		ao.readMailBox();

	}

}

import java.util.concurrent.Semaphore;


public class AvoidObstacleThread extends Thread implements ILogger {
	final int MAX_DISTANCE = 15;

	final int MAX_ANGLE = 90;

	final int MAX_RADIUS = 0;

	protected String robotName;

	protected MyRobot theRobot;
	
	private Semaphore semaphore;
	
	private boolean hit;

	public enum States{
		Running, Waiting, Ending
	};
	
	private States currentState;

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public AvoidObstacleThread(MyRobot robot) {
		this.currentState = States.Waiting;
		this.theRobot = robot;
		this.semaphore = new Semaphore(0);
		this.hit = false;

	}
	
	public boolean readSensor(){
		return this.theRobot.GetTouchSensor();
	}
	
	public boolean hit(){
		return this.hit;
	}
	
	public void resetHit(){
		this.hit = false;
	}


	public void doAvoidObstacle() {
		while(this.currentState != States.Ending){
			if(this.currentState == States.Waiting){
				if(readSensor()){
					this.theRobot.Parar(true);
					this.hit=true;
				}
			}
			if(this.currentState == States.Running){
				try {
					this.semaphore.acquire();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				this.theRobot.Reta(-MAX_DISTANCE);
				this.theRobot.CurvarEsquerda(MAX_RADIUS, MAX_ANGLE);
				this.theRobot.Parar(false);
				this.semaphore.release();
			}
		}
	}
	
	public void myWait(){
		//fica bloqueado sem fazer acção nenhuma
		//até que a sua maquina de estados sofra alterações
		try {
			this.log("---------------------estou a espera no VAGUEAR---------------------");
			this.semaphore.acquire();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//experimentar com gestor se funciona
//		this.semaphore.release();
	}
	
	public void myPause(){
		//pausa o trabalho do vaguear, sem terminar o ciclo
		this.currentState = States.Waiting;
	}
	
	public void myResume(){
		//inicia o comportamento do vaguear
		this.currentState = States.Running;
		this.semaphore.release();
		this.log("---------------------estou a correr no VAGUEAR---------------------");
	}
	
	public void myEnding(){
		//encerra o trabalho da thread
		this.currentState = States.Ending;
		this.log("---------------------estou acabar o VAGUEAR---------------------");
	}
	
	@Override
	public void run(){
		
		
		
	}

}

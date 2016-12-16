import java.util.concurrent.Semaphore;

public class SegueParede extends Thread implements ILogger {
	
	final static int DISTANCIA_CONTROLO = 10;//cm

	private MyRobot robot;
	
	private Semaphore semaphore;
	
	private int lastDistance;

	private enum States {
		Waiting, Running, Reading, Ending
	}

	private States currentState;

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public SegueParede(MyRobot robot, Semaphore semaphore) {
		// TODO Auto-generated constructor stub
		this.robot = robot;
		this.currentState = States.Waiting;
		this.semaphore = semaphore;
		this.lastDistance = 0;
	}

	public void myPause() {
		this.currentState = States.Waiting;
	}

	public void myResume() {
		this.currentState = States.Running;
		this.semaphore.release();
	}

	public void myEnding() {
		this.currentState = States.Ending;
	}
	
	private void myReading(){
		this.lastDistance = this.robot.GetSensorUS();
	}
	
	public int getLastDistance(){
		return this.lastDistance;
	}
	
	private void myAction(){
		
		try {
			this.semaphore.acquire();
			this.robot.Reta(DISTANCIA_CONTROLO);
			//espera que ande a distancia de controlo
			Thread.sleep(1000);
			int aux = this.robot.GetSensorUS();
			if(aux > 100){
				this.currentState = States.Waiting;
			}else{
				double radianos = Math.atan((getLastDistance()-aux)/DISTANCIA_CONTROLO);
				double degrees = Math.toDegrees(radianos);
				this.robot.CurvarEsquerda(0, (int)degrees);
				this.lastDistance = aux;
				//falta fazer verificação de acertos nos angulos
				//caso o robot se esteja afastar da parede -------> CURVAR DIREITA
			}
			
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		

		
	}

	@Override
	public void run() {
		while (this.currentState != States.Ending) {
			switch (this.currentState) {
			case Waiting:
				//estado inicial quando se liga o robot na interface grafica
				break;

			case Reading:
				myReading();
				break;

			case Running:
				myAction();
				break;

			default:
				break;
			}

		}

	}

}

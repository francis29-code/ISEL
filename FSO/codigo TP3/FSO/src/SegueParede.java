import java.util.concurrent.Semaphore;

public class SegueParede extends Thread implements ILogger {
	
	private int distCtrl;

	private MyRobot robot;
	
	private Semaphore semaphore;
	
	private int lastDistance;

	private enum States {
		Waiting, Running, Ending, Control
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
		this.distCtrl = 0;
		this.robot = robot;
		this.currentState = States.Waiting;
		this.semaphore = semaphore;
		this.lastDistance = 0;
	}

	public void myPause() {
		this.currentState = States.Waiting;
	}
	
	public void setDistanceCTRL(int distance){
		this.distCtrl = distance;
	}

	public void myResume() {
		this.currentState = States.Running;
		this.semaphore.release();
	}

	public void myEnding() {
		this.currentState = States.Ending;
	}
	
	public void myControlState(){
		this.currentState = States.Control;
		this.semaphore.release();
	}
	
//	private void myReading(){
//		this.lastDistance = this.robot.GetSensorUS();
//	}
	public void settLastDistance(int distance){
		this.lastDistance = distance;
	}
	
	private void myControl(){
		
		try {
			this.semaphore.acquire();
			this.robot.Reta(this.distCtrl);
			//espera que ande a distancia de controlo
			Thread.sleep((int)(this.distCtrl * 5.0 / 100.0));
			this.currentState = States.Running;
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	private void myAction(){
		int aux = this.robot.GetSensorUS();
		if(aux < 100 && aux > 20){
			this.currentState = States.Waiting;
		}else{
			double radianos = Math.atan((this.lastDistance-aux)/this.distCtrl);
			double degrees = Math.toDegrees(radianos);
			this.robot.CurvarEsquerda(0, (int)degrees);
			this.lastDistance = aux;
			//falta fazer verificação de acertos nos angulos
			//caso o robot se esteja afastar da parede -------> CURVAR DIREITA
		}
		
	
	}

	@Override
	public void run() {
		while (this.currentState != States.Ending) {
			switch (this.currentState) {
			case Waiting:
				//estado inicial quando se liga o robot na interface grafica
				break;
				
			case Control:
				myControl();
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

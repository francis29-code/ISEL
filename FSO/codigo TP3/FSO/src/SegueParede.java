import java.util.concurrent.Semaphore;

public class SegueParede extends Thread implements ILogger {
	
	private int distCtrl;

	private MyRobot robot;
	
	private Semaphore semaphore;
	
	private int lastDistance, firstDistance;

	public enum States {
		Dorment, Running, Ending, Control, waitDistance, waitSecondDistance
	}

	private States currentState;
	
	public int currentState(){
		switch(this.currentState){
		case Dorment:
			return 0;
			
		case Running:
			return 1;
			
		case Ending:
			return 2;
			
		case Control:
			return 3;
			
		case waitDistance:
			return 4;
			
		case waitSecondDistance:
			return 5;
			
		default:
			break;
		}
		return -1;
	}

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
		this.currentState = States.Dorment;
		this.semaphore = semaphore;
		this.lastDistance = 0;
		this.firstDistance = 0;
	}

	public void myPause() {
		this.currentState = States.Dorment;
	}
	
	public void setDistanceCTRL(int distance){
		this.distCtrl = distance;
	}
	
	public int getDistanceCTRL(){
		return this.distCtrl;
	}

	public void myResume() {
		this.currentState = States.waitDistance;
	}

	public void myEnding() {
		this.currentState = States.Ending;
	}
	
	public void setLastDistance(int distance){
		this.lastDistance = distance;
		this.semaphore.release();
	}
	
	private void myWait(){
		if(this.lastDistance != 0){
			this.currentState = States.Control;
		}
	}
	
	private void myControl(){
		this.log("ENTREI NO CONTROLO SEGUE PAREDE");
		if(this.firstDistance == 0){
			try {
				this.semaphore.acquire();
				this.robot.Reta(this.distCtrl);
				//espera que ande a distancia de controlo
				Thread.sleep((this.distCtrl * 5/100)*1000);
				this.robot.Parar(true);
				//troca as variaveis para calculos de DELTA
				this.firstDistance = this.lastDistance;
				//reset variavel para não confundir verificações
				this.lastDistance = 0;
				this.currentState = States.waitSecondDistance;
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}else{
			this.currentState = States.waitSecondDistance;
		}

	}
	
	private void myAction() {
		this.log("ENTREI NA ACÇÃO SEGUE PAREDE");
		if(this.lastDistance !=0){
			try {
				this.semaphore.acquire();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			double radianos = Math.atan((this.lastDistance-this.firstDistance)/this.distCtrl);
			double degrees = Math.toDegrees(radianos);
			this.robot.CurvarEsquerda(0, (int)degrees);
			//verificaçoes futuras para ajustamento correto
			//CURVAR DIREITA
			this.robot.Reta(this.distCtrl);
			try {
				Thread.sleep((this.distCtrl*5/100)*1000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			this.firstDistance = this.lastDistance;
			this.lastDistance = 0;
			this.currentState = States.waitDistance;
		}
	}

	@Override
	public void run() {
		while (this.currentState != States.Ending) {
			switch (this.currentState) {
			
			case Dorment:
				
				break;
				
			case waitDistance:
				myWait();
				break;
				
			case Control:
				myControl();
				break;
				
			case waitSecondDistance:
				myAction();
				break;
	
			default:
				break;
			}

		}

	}

}

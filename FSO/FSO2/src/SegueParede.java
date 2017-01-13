import java.util.concurrent.Semaphore;

public class SegueParede extends Thread implements ILogger {
	
	private int distCtrl;

	private MyRobot robot;
	
	private Semaphore acessoRobot, ownSemaphore;
	
	private int lastDistance, currentDistance, currentSleep;

	private States currentState;
	
	private boolean checked;

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public SegueParede(MyRobot robot, Semaphore semaphore) {
		this.setName("Segue");
		this.robot = robot;
		this.acessoRobot = semaphore;
		this.lastDistance = 0;
		this.currentDistance = 0;
		this.distCtrl = 0;
		this.currentSleep = 0;
		this.checked = false;
		this.currentState = States.Waiting;
		this.ownSemaphore = new Semaphore(0);
	}
	
	
	public void myPause(){
		this.currentState = States.Waiting;
		this.robot.Parar(true);
	}
	
	
	public void setControlDist(int distance) {
		// TODO Auto-generated method stub
		this.distCtrl = distance;
		setSleepTime(distance);
	}
	
	private void setSleepTime(int distance){
		//distancia de controlo como parametro
		this.currentSleep = distance*5/100;
	}
	
	public int getSleepTime(){
		return this.currentSleep;
	}
	
	public void updateCheck(boolean check){
		this.checked = check;
		if(!this.checked){
			myPause();
			this.log("MANDEI PARA O WAITING SEGUE");
		}else{
//			myResume();
			myOwnReading();
		}
	}
	
	public void setCurrentDistance(int distanceRead){
		this.currentDistance = distanceRead;
	}
	
	public void myResume(){
		this.ownSemaphore.release();
		this.currentState = States.WaitDistance;
	}
	
	private void waitDistance(){
		if(this.currentDistance != 0){
			try {
				this.acessoRobot.acquire();
				this.currentState = States.Control;
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	private void myOwnReading(){
		int distance;
		distance = this.robot.GetSensorUS();
		this.log("DISTANCIA LIDA: " + distance);
		if(distance < 100 && distance > 20){
			this.log("ENTROU NO IF");
			setCurrentDistance(distance);
			try {
				this.acessoRobot.acquire();
			} catch (InterruptedException e) {
				
				e.printStackTrace();
			}
			this.log("PASSEI O ACQUIRE");
			this.currentState = States.Control;
		}
		
		this.log("estado do automato: " + this.currentState);
	}
	
	private void myControl(){
		this.log("ENTREI NO CONTROLO");
		this.robot.Reta(this.distCtrl);
		this.robot.Parar(false);
		//liberta o robot
		this.acessoRobot.release();
		
		this.log("ESTADO CONTROLO");
		
		if(this.lastDistance ==0){
			this.lastDistance = this.currentDistance;
			this.currentDistance = 0;
		}
		
		//prints debug
		this.log("distancia atual : " + this.currentDistance);
		this.log("distancia antiga : " + this.lastDistance);
		
		try {
			Thread.sleep((getSleepTime()*1000)+2000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		setCurrentDistance(this.robot.GetSensorUS());
		
		this.currentState = States.Running;
	}
	
	private void myAction(){
		try {
			this.acessoRobot.acquire();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		//prints debug
		this.log("ESTADO ACTION");
		this.log("distancia atual : " + this.currentDistance);
		this.log("distancia antiga : " + this.lastDistance);
		
		
		double radianos = Math.atan((this.lastDistance-this.currentDistance)/this.distCtrl);
		double degrees = Math.toDegrees(radianos);
		if(this.lastDistance < this.currentDistance){
			this.robot.CurvarDireita(0, (int)degrees);
		}else{
			this.robot.CurvarEsquerda(0, (int)degrees);
		}
		//liberta o robot para um outro comportamento apanhar se indicado
		this.acessoRobot.release();
		this.currentState = States.Reading;
		this.lastDistance = this.currentDistance;
		this.currentDistance = 0;
	}
	
	public States currentState(){
		return this.currentState;
	}
	
	public void readingDistance(){
		this.log("DISTANCE READ: " + this.robot.GetSensorUS());
	}
	
	
	@Override
	public void run() {
		while(this.currentState != States.Ending){
			switch(this.currentState){
			case Waiting:
				this.log("ESTU NO WAITING DO SEGUEPAREDE");
				this.log("ESTADO A PRINTAR " +this.currentState);
				try{
					this.ownSemaphore.acquire();
				}catch(Exception e){
					e.printStackTrace();
				}
				break;
				
				
//			case WaitDistance:
//				waitDistance();
//				break;
				
			case Reading:
				this.log("ESTADO A PRINTAR " +this.currentState);
				myOwnReading();
				break;
				
			case Control:
				this.log("ESTADO A PRINTAR " +this.currentState);
				myControl();
				break;
//				
			case Running:
				this.log("ESTADO A PRINTAR " +this.currentState);
				myAction();
				break;
				

			default:
				break;
			}
		}
	}

}

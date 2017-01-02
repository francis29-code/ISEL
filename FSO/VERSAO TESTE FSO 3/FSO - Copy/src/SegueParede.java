import java.util.concurrent.Semaphore;

public class SegueParede extends Thread implements ILogger {
	
	private int distCtrl;

	private MyRobot robot;
	
	private Semaphore semaphore;
	
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
		this.semaphore = semaphore;
		this.lastDistance = 0;
		this.distCtrl = 0;
		this.currentSleep = 0;
		this.checked = false;
	}
	
	
	public void myPause(){
		this.currentState = States.Waiting;
	}
	
	
	public void setControlDist(int distance) {
		// TODO Auto-generated method stub
		this.distCtrl = distance;
		setSleepTime(distance);
	}
	
	private void setSleepTime(int distance){
		this.currentSleep = distance*5/100;
	}
	
	public int getSleepTime(){
		return this.currentSleep;
	}
	
	public void updateCheck(boolean check){
		this.checked = check;
		if(!this.checked){
			this.currentState = States.Waiting;
			this.log("MANDEI PARA O WAITING SEGUE");
		}
	}
	
	@Override
	public void run() {
		while(this.currentState != States.Ending){
			switch(this.currentState){
			case Waiting:
				if(this.checked){
					this.currentState = States.Running;
				}
				break;
				
			case Control:
				
				break;
				
			case Running:
				
				break;
				

			default:
				break;
			}
		}
	}

}

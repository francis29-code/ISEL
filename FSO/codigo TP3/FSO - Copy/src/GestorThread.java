import java.util.concurrent.Semaphore;

public class GestorThread extends Thread implements ILogger{
	
	
	private States currentState;
	
	private VaguearT vaguear;
	private AvoidObstacleThread evitar;
	private SegueParede segue;
	private MyRobot robot;
	private boolean checked;
	private ThreadKeeper threadContainer;
	private int readDistance;
	
	private Semaphore ownSemaphore;
//	private int currentSleep;
//	final static int SLEEP_TIME_SENSOR = 800;
	
	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public GestorThread(MyRobot robot, ThreadKeeper lista) {
		this.setName("Gestor");
		this.checked = false;
		this.threadContainer = lista;
		this.currentState = States.Init;
		this.vaguear = (VaguearT) this.threadContainer.getThread("Vaguear");
//		this.evitar = (AvoidObstacleThread) this.threadContainer.getThread("Evitar");
		this.segue = (SegueParede) this.threadContainer.getThread("Segue");
		this.readDistance = 0;
		this.robot = robot;
		this.ownSemaphore = new Semaphore(0);
	}
	
	private void myPause(){
		this.currentState = States.Init;
	}
	
	private void myResume(){
		this.currentState = States.Check;
		this.ownSemaphore.release();
	}
	
	public void updateCheck(boolean check){
		this.checked = check;
		if(!this.checked){
			myPause();
			this.log("MANDEI PARA O INIT DO GESTOR");
		}else{
			myResume();
		}
	}

	@Override
	public void run() {

		while(this.currentState != States.Ending){
			
			int readDistance;
			readDistance = 0;
			
			switch(this.currentState){
			case Init:
				try {
					this.ownSemaphore.acquire();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
				
			case Check:
				readDistance = this.robot.GetSensorUS();
				//estado em que verifica e atribui prioridades
				//escolhe entre o comportamento vaguear e o seguir parede
				if(readDistance < 100 && readDistance > 20){
					this.currentState = States.SegueParede;
				}else{
					this.currentState = States.Vaguear;
				}
				break;
				
				
			case SegueParede:
				//comunica distancia lida para o comportamento segue parede
				//quando manda andar, tem de espera o tempo suficiente para voltar a ler o sensor.
				try {
					this.segue.setCurrentDistance(readDistance);
					Thread.sleep(this.segue.getSleepTime()*1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				
				this.currentState = States.Check;
				
				break;
				
				
			case Vaguear:
				//efetivamente ordena o vaguear a trabalhar
				if(this.vaguear.currentState() == States.Running){
					this.currentState = States.Check;
				}else if(this.vaguear.isChecked()){
					this.vaguear.myWork();
					this.currentState = States.Check;
				}else{
					this.currentState = States.Check;
				}
				break;
				
				
			default:
				break;
			}
		}

	}

}

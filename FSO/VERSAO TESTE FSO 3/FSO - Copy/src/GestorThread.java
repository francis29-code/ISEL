public class GestorThread extends Thread implements ILogger{
	
	
	private States currentState;
	
	private VaguearT vaguear;
	private AvoidObstacleThread evitar;
	private SegueParede segue;
	private MyRobot robot;
	private boolean checked;
	private ThreadKeeper threadContainer;
//	private Semaphore semaphore;
	private int currentSleep;
	final static int SLEEP_TIME_SENSOR = 800;
	
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
		this.evitar = (AvoidObstacleThread) this.threadContainer.getThread("Evitar");
	}
	
	public void updateCheck(boolean check){
		this.checked = check;
		if(!this.checked){
			this.currentState = States.Init;
			this.log("MANDEI PARA O INIT");
		}
	}

	@Override
	public void run() {
		while(this.currentState != States.Ending){
			switch(this.currentState){
			case Init:
				if(this.checked){
					this.currentState = States.Check;
				}
				break;
			case Check:
				Thread lastThread = this.threadContainer.getLastThread();
				String threadName = lastThread.getName();
				switch(threadName){
				case "Vaguear":
					this.log("-------------------------------------------------PAREI O VAGUEAR");
					VaguearT vaguearT = (VaguearT) lastThread;
					try{
						Thread.sleep(vaguearT.getSleepTime());
					}catch(Exception e){
						e.printStackTrace();
					}
				case "Segue":
					this.log("-------------------------------------------------PAREI O SEGUE PAREDE");
					SegueParede segue = (SegueParede) lastThread;
					try{
						Thread.sleep(segue.getSleepTime());
					}catch(Exception e){
						e.printStackTrace();
					}
					break;
				}
				
				
				
				if(this.evitar.hadContact()){
					this.log("TIVE CONTACTO------------------------------------");

					switch(threadName){
					case "Vaguear":
						this.log("-------------------------------------------------PAREI O VAGUEAR");
						VaguearT vaguearT = (VaguearT) lastThread;
						vaguearT.myPause();
					case "Segue":
						this.log("-------------------------------------------------PAREI O SEGUE PAREDE");
						SegueParede segue = (SegueParede) lastThread;
						segue.myPause();
						break;
					}
					this.currentState = States.Evitar;
				}
				
				else{
					if(this.vaguear.isChecked()){
						this.currentState=States.Vaguear;
					}else{
						this.currentState = States.Check;
					}
				}
				break;
				
			case Vaguear:
				this.log("ESTOU NO VAGUEAR GESTOR");
				System.out.println("check state: " + this.vaguear.currentState());
					
				if(this.vaguear.currentState() != States.Running){
//					this.log("ENTREI NO STATE != RUNNING");
					this.threadContainer.priotirizeThread("Vaguear");
					this.vaguear.workPermission();
				}else{
					this.currentState = States.Check;
				}
				
				break;
			
			case Evitar:
				this.log("ESTOU NO EVITAR GESTOR");
				this.threadContainer.priotirizeThread("Evitar");
				this.evitar.doAction();
				try {
					Thread.sleep(this.evitar.totalSleepTime()+500);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				this.currentState = States.Check;
				
				break;
				
			default:
				break;
			}
		}

	}

}

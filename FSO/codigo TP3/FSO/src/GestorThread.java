import java.util.concurrent.Semaphore;

public class GestorThread extends Thread implements ILogger{
	
	public enum States {Vaguear, Evitar, SegueParede, Terminar, Check, Init};
	private States currentState;
	
	private VaguearT vaguear;
	private AvoidObstacleThread evitar;
	private SegueParede segue;
	private MyRobot robot;
//	private Semaphore semaphore;
	
	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public GestorThread(MyRobot robot, VaguearT vaguear, AvoidObstacleThread avoid, SegueParede segue) {
		this.currentState = States.Init;
//		this.semaphore = new Semaphore(0);
		this.vaguear = vaguear;
		this.evitar = avoid;
		this.segue = segue;
		this.robot = robot;

	}
	
	public void myWait(){
		//fica bloqueado sem fazer acção nenhuma
		//até que a sua maquina de estados sofra alterações
//		try {
//			
//			this.semaphore.acquire();
////			this.log("---------------------estou a espera no GESTOR---------------------");
//			//apena coloca o evitar a ler se foi dada permissão de troca
//			//para o estado Vaguears
//			this.evitar.myStart();
//		} catch (InterruptedException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
		//experimentar com gestor se funciona
//		this.semaphore.release();
	}
	
	public void myPause(){
		//pausa o trabalho do vaguear, sem terminar o ciclo
		this.currentState = States.Init;
		//quando o gestor é disabled, todas as threads ficam em pausa
		this.vaguear.myPause();
		this.evitar.myPause();
		this.segue.myPause();
//		this.log("---------------------pausei no GESTOR---------------------");
	}
	
	public void myResume(){
		//inicia o comportamento do vaguear
		this.currentState = States.Vaguear;
		this.evitar.myStart();
//		this.semaphore.release();
//		this.log("---------------------estou a correr no GESTOR---------------------");
	}
	
	public void myEnding(){
		//encerra o trabalho da thread
		this.currentState = States.Terminar;
//		this.log("---------------------estou acabar o GESTOR---------------------");
	}
	
	
	@Override
	public void run() {
		
		int distanceRead;
		distanceRead =0;

		while (this.currentState != States.Terminar) {
			switch (this.currentState) {
			
			case Init:
				//estado inicial quando se liga o robot na interface grafica
				myWait();
				break;
			
			case Check:
//				this.log("estado: check");
				if(this.evitar.hit()){
					this.evitar.resetHit();
					this.vaguear.myPause();
					this.currentState = States.Evitar;
				}
				
				distanceRead = this.robot.GetSensorUS();
				if(distanceRead>20 && distanceRead<100){
					this.vaguear.myPause();
					this.segue.settLastDistance(distanceRead);
					this.currentState = States.SegueParede;
				}

				break;

			case Vaguear:
				this.log("estado: Vaguear");
				this.vaguear.myResume();
				this.currentState = States.Check;
				break;
				
			case Evitar:
				this.log("estado: Evitar");
				this.evitar.myResume();
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				this.currentState = States.Vaguear;
				break;
				
			case SegueParede:
				this.log("estado: SegueParede");
				this.segue.myControlState();
				break;
			default:
				break;
				
			}

		}

	}

}

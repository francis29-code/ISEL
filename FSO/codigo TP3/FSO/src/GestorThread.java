import java.util.concurrent.Semaphore;

public class GestorThread extends Thread implements ILogger{
	
	public enum States {Vaguear, Evitar, SegueParede, Terminar, Check, Init};
	private States currentState;
	private States lastState;
	
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
		this.lastState = null;
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
		boolean aux;
		aux = false;

		while (this.currentState != States.Terminar) {
			switch (this.currentState) {
			
			case Init:
				//estado inicial quando se liga o robot na interface grafica
				myWait();
				break;
			
			case Check:
				//ler sensor com a mesma proporcianalidade de tempo da distancia de controlo
				//1 segundo
				
				try {
					Thread.sleep((this.segue.getDistanceCTRL() *5/100)*1000);
				} catch (InterruptedException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				
//				this.log("estado: check");
				distanceRead = this.robot.GetSensorUS();
				this.log(""+distanceRead);
				aux = (distanceRead>20 && distanceRead<100);
				if(this.evitar.hit()){
					this.evitar.resetHit();
					this.vaguear.myPause();
					this.currentState = States.Evitar;
				}
				else if(aux){
					this.log("ENTREI NO SEGUIR PAREDE-------------------------");
					this.vaguear.myPause();
					this.segue.myResume();
					this.currentState = States.SegueParede;
				}
				else if(!(this.evitar.hit() || aux)){
					this.currentState = States.Vaguear;
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
					Thread.sleep(4000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				this.currentState = States.Check;
				break;
				
			case SegueParede:
//				this.log("estado: SegueParede");
				if(this.segue.currentState() == 5){
					//se for igual ao waitdistance
					this.log("ENTREI NO SEGUIR PAREDE-------------------------ESTADO 5");
					this.segue.setLastDistance(distanceRead);
					this.currentState = States.Check;
					break;
					
				}else{
//					this.vaguear.myPause();
					this.log("ENTREI NO SEGUIR PAREDE-------------------------ESTADO 1");
					this.segue.setLastDistance(distanceRead);
					this.currentState = States.Check;
					break;
				}
				
			default:
				break;
				
			}

		}

	}

}

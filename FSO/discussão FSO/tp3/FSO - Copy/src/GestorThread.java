import java.util.ArrayList;
import java.util.Arrays;
import java.util.concurrent.Semaphore;

public class GestorThread extends Thread implements ILogger {

	private States currentState;

	private VaguearT vaguear;
	private SegueParede segue;
	private MyRobot robot;
	private boolean checked;
	private ThreadKeeper threadContainer;
	private CaixaCorreio caixa;
	private Semaphore ownSemaphore;
	private int lista[];

	@Override
	public String log(String message, Object... args) {
		String aux1, aux2;
		aux1 = String.format(message, args);

		aux2 = String.format("[%s] %s", this.getName(), aux1);

		System.out.println(aux2);

		return aux2;
	}

	public GestorThread(MyRobot robot, ThreadKeeper lista, CaixaCorreio caixa) {
		this.setName("Gestor");
		this.checked = false;
		this.threadContainer = lista;
		this.currentState = States.Init;
		this.vaguear = (VaguearT) this.threadContainer.getThread("Vaguear");
		this.segue = (SegueParede) this.threadContainer.getThread("Segue");
		this.robot = robot;
		this.ownSemaphore = new Semaphore(0);
		this.lista = new int[5];
		this.caixa = caixa;
	}
	
	private void addToArray(int distancia){
		for(int i=lista.length-1; i>0;i--){
			lista[i] = lista[i-1];
		}
		
		lista[0] = distancia;
	}
	
	private int getDistancia(){
		int aux;
		aux =0;
		//aplicar filtro de mediana
		while(aux < lista.length){
			addToArray(this.robot.GetSensorUS());
			aux++;
		}
		
		int lista2[] = lista;
		Arrays.sort(lista2);
		
		return lista2[lista2.length/2];
		
	}

	private void myPause() {
		this.currentState = States.Init;
		this.segue.myPause();
	}

	private void myResume() {
		this.currentState = States.fillArray;
		this.ownSemaphore.release();
	}

	public void updateCheck(boolean check) {
		this.checked = check;
		if (!this.checked) {
			myPause();
			this.log("MANDEI PARA O INIT DO GESTOR");
		} else {
			myResume();
		}
	}

	@Override
	public void run() {
		while (this.currentState != States.Ending) {
			int distancia;
			distancia =0;
			switch (this.currentState) {
			case Init:
				try {
					this.ownSemaphore.acquire();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
				}
			case fillArray:
				int aux;
				aux =0;
				//aplicar filtro de mediana
				while(aux < lista.length){
					addToArray(this.robot.GetSensorUS());
					aux++;
				}
				this.currentState = States.SegueParede;
				break;
			case SegueParede:
				distancia = getDistancia();
				if(distancia <100){
					this.caixa.inserirElemento(new Integer(distancia));
					this.currentState = States.SegueParede;
				}else{
					this.currentState = States.Vaguear;
					if(this.segue.isChecked()){
						this.segue.myPause();
					}
					if(this.vaguear.isChecked()){
						this.vaguear.myResume();
					}
				}
				try {
					Thread.sleep(250);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			case Vaguear:
				distancia = getDistancia();
				if(distancia <100){
					this.caixa.inserirElemento(new Integer(distancia));
					this.currentState = States.SegueParede;
					if(this.segue.isChecked()){
						this.segue.myResume();
					}
					if(this.vaguear.isChecked()){
						this.vaguear.myPause();
					}
				}else{
					this.currentState = States.Vaguear;
				}
				try {
					Thread.sleep(250);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			default:
				break;
			}
		}
	}

}

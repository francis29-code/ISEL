import java.io.IOException;

public class Gestor {

	// tempo de espera para ler o proprio ficheiro
	final int SLEEP_TIME = 1000;
	// caixas de correio para cada processo
	private MailBox mailGestor, mailVaguear, mailEvitar;
	private String jarAvoid = "java -jar C:\\Users\\Denga\\Desktop\\JAR FILES\\avoid.jar";
	private String jarVaguear = "java -jar C:\\Users\\Denga\\Desktop\\JAR FILES\\vaguear.jar";
	private Process processVaguear, processAvoid;
	private Runtime runtime;
	private String prefixGestor = "PG";
	private String prefixAvoid = "PA";
	private String prefixVaguear = "PV";
	int estado;
	static private final int init = 0;
	static private final int vaguear = 1;
	static private final int avoid = 2;
	static private final int closeVaguear = 3;
	static private final int closeAvoid = 4;
	static private final int Terminar = 5;

	public Gestor() {
		// TODO Auto-generated constructor stub
		this.mailGestor = new MailBox("gestor.dat");
		this.mailEvitar = new MailBox("evitar.dat");
		this.mailVaguear = new MailBox("vaguear.dat");
		this.runtime = Runtime.getRuntime();

	}

	public void launchProcesses() {

		while (estado != Terminar) {
			switch (estado) {
			case init:
				System.out.println("estado: init");
				this.processAvoid = null;
				this.processVaguear = null;
				try {
					
					//escreve na caixa de correio do vaguear uma permissao
					this.mailVaguear.write(prefixGestor + "start");
					
					
					// caminho do jar vaguear
					this.processVaguear = this.runtime.exec(jarVaguear);
					System.out.println("duvida: " + this.processVaguear.isAlive());
				} catch (IOException e) {
					e.printStackTrace();
				}

				try {
					//pequeno delay para garantir o lançamento do vaguear
					Thread.sleep(500);
				} catch (InterruptedException e) {

					e.printStackTrace();
				}
				try {
					// caminho do jar do evitar
					this.processAvoid = this.runtime.exec(jarAvoid);
					System.out.println("duvida2: " + this.processAvoid.isAlive());
				} catch (IOException e) {
					e.printStackTrace();
				}
				
				estado = vaguear;
				
				break;

			case vaguear:
				System.out.println("estado vaguear");
				try {
					//pequeno delay para garantir o lançamento do vaguear
					Thread.sleep(500);
				} catch (InterruptedException e) {

					e.printStackTrace();
				}
				System.out.println("read do gestor: " + mailGestor.read());
				if(this.mailGestor.read().equals(prefixVaguear+"sstop")){
					this.mailEvitar.write(prefixGestor + "start");
					estado = avoid;
					break;
				}else{
					estado = vaguear;
					break;
				}
				

			case avoid:
				System.out.println("estado avoid");
				try {
					//pequeno delay para garantir o lançamento do vaguear
					Thread.sleep(500);
				} catch (InterruptedException e) {

					e.printStackTrace();
				}
				if(this.mailGestor.read().equals(prefixAvoid+"sstop")){
					this.mailVaguear.write(prefixGestor + "start");
					estado = vaguear;
				}else{
					estado = avoid;
					break;
				}
				
				
				break;

			case closeVaguear:

				break;

			case closeAvoid:

				break;

			}

		}

	}
	
	
	public static void main(String []args){
		Gestor ge = new Gestor();
		ge.launchProcesses();
	}

}

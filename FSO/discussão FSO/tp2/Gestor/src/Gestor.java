import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Gestor {

	// tempo de espera para ler o proprio ficheiro
	private static final int SLEEP_TIME = 1000;
	// caixas de correio para cada processo
	private MailBox mailGestor, mailVaguear, mailEvitar;
	private String jarAvoid = "C:\\Users\\Denga\\Desktop\\JARFILES\\evitar.jar";
	private String jarVaguear = "C:\\Users\\Denga\\Desktop\\JARFILES\\vaguear.jar";
	private Process processVaguear, processAvoid;
	private String[] arguments = new String[]{"java","-jar","GUIA4",""+RobotLego.S_2,"true"};
	private String prefixGestor = "PG";
	private String prefixAvoid = "PA";
	private String prefixVaguear = "PV";
	private String prefixGUI = "PGUI";
	private int estado;
	static private final int init = 0;
	static private final int vaguear = 1;
	static private final int avoid = 2;
	static private final int closeVaguear = 3;
	static private final int closeAvoid = 4;
	static private final int Terminar = 5;

	public Gestor() {
		this.mailGestor = new MailBox("gestor.dat");
		this.mailEvitar = new MailBox("evitar.dat");
		this.mailVaguear = new MailBox("vaguear.dat");
		this.estado = init;

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
					
					//agumentos para o lançamento do processo
					List<String> argsVaguear;
					argsVaguear = new ArrayList<String>();
					argsVaguear.add(arguments[0]);
					argsVaguear.add(arguments[1]);
					argsVaguear.add(jarVaguear);
					argsVaguear.add(arguments[2]);
					argsVaguear.add(arguments[3]);
					argsVaguear.add(arguments[4]);
					argsVaguear.add("false");
					
					// caminho do jar vaguear
					ProcessBuilder pbVaguear;
					pbVaguear = new ProcessBuilder(argsVaguear);
					pbVaguear.redirectErrorStream(true);
					pbVaguear.inheritIO();
					this.processVaguear = pbVaguear.start();
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
					//argumentos para o lançamento do processo
					List<String> argsAvoid;
					argsAvoid = new ArrayList<String>();
					argsAvoid.add(arguments[0]);
					argsAvoid.add(arguments[1]);
					argsAvoid.add(jarAvoid);
					argsAvoid.add(arguments[2]);
					argsAvoid.add(arguments[3]);
					argsAvoid.add(arguments[4]);
					argsAvoid.add("false");
					// caminho do jar vaguear
					ProcessBuilder pbAvoid;
					pbAvoid = new ProcessBuilder(argsAvoid);
					pbAvoid.redirectErrorStream(true);
					pbAvoid.inheritIO();
					this.processAvoid = pbAvoid.start();
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
				if(this.mailGestor.read().equals(prefixGUI + "para")){
					this.mailGestor.eraseContent();
					//processos substituidos por mensagem na caixa de correio
					try {
						this.mailEvitar.write(prefixGestor+"sstop");
						this.processAvoid.waitFor();
						this.mailVaguear.write(prefixGestor+"sstop");
						this.processVaguear.waitFor();
						estado = Terminar;
						break;
					} catch (Exception e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				
				else if(this.mailGestor.read().equals(prefixVaguear+"sstop")){
					this.mailGestor.eraseContent();
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
				if(this.mailGestor.read().equals(prefixGUI + "para")){
					this.mailGestor.eraseContent();
					//processos substituidos por mensagem na caixa de correio
					try {
						this.mailEvitar.write(prefixGestor+"sstop");
						this.processAvoid.waitFor();
						this.mailVaguear.write(prefixGestor+"sstop");
						this.processVaguear.waitFor();
						estado = Terminar;
						break;
					} catch (Exception e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				if(this.mailGestor.read().equals(prefixAvoid+"sstop")){
					this.mailGestor.eraseContent();
					this.mailVaguear.write(prefixGestor + "start");
					estado = vaguear;
				}else{
					estado = avoid;
					break;
				}

			}

		}

	}
	
	public static void main(String []args){
		Gestor ge = new Gestor();
		ge.launchProcesses();
	}
	
	

}

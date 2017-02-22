import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Scanner;

public class RobotPlayer extends Thread implements ILogger{

	private MyRobot robot;
//	PrintWriter writerDir;
	private Writer writerDir = null;
	private File file;
	
	private String url;
	private estados estado;
	
	private ArrayList<String> playinv;
	
	public enum estados{
		waiting,Play,PlayInverse,Stop,ending;
	}
	
	
	
	public RobotPlayer(MyRobot robot){
		this.robot = robot;
		url = "C:\\Users\\Denga\\Desktop\\workspace\\FSO2\\directions";
		file = new File(url+"directions.txt");
		playinv = new ArrayList<>();
		
		try {
		    writerDir = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file), "utf-8"));
		
		} catch (IOException ex) {
		  // report
		}
		estado = estados.waiting;
	}
	
	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}
	
	public void recordDirections(String data){
		
		try {
			writerDir.write(data + "\n");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	    
	}
	
	public void play() throws FileNotFoundException{
		
		Scanner sc= new Scanner(file);
		String theString = sc.nextLine();
		
		while (sc.hasNextLine()) {
			theString = theString + "\n" + sc.nextLine();
			
		}
		String[] aux = theString.split("\n");
		for(int i = 0; i < aux.length; i++){
			if(aux[i].contains("reta")){
				String x = aux[i].substring(aux[i].indexOf(':') + 1);
				int y = Integer.parseInt(x);
				log("reta: "+y);
				robot.Reta(y,false);
				
				
			}
			if(aux[i].contains("curvardireita")){
				String raio = aux[i].substring(aux[i].indexOf(':') + 1, aux[i].indexOf(','));
				String angulo = aux[i].substring(aux[i].indexOf(',') + 1);
				int r = Integer.parseInt(raio);
				int a = Integer.parseInt(angulo);
				log("curvardireita: raio ="+r+" angulo ="+a);
				robot.CurvarDireita(r, a,false);
				
			}
			if(aux[i].contains("curvaresquerda")){
				String raio = aux[i].substring(aux[i].indexOf(':') + 1, aux[i].indexOf(','));
				String angulo = aux[i].substring(aux[i].indexOf(',') + 1);
				int r = Integer.parseInt(raio);
				int a = Integer.parseInt(angulo);
				log("curvaresquerda: raio ="+r+" angulo ="+a);
				robot.CurvarEsquerda(r, a,false);
				
			}
			if(aux[i].contains("parar")){
				String y = aux[i].substring(aux[i].indexOf(':') + 1);
				boolean x = Boolean.parseBoolean(y);
				log("STOP: "+x);
				robot.Parar(x);
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}
		
		sc.close();
	}
	
	public void playInverse() throws FileNotFoundException{
		Scanner sc= new Scanner(file);
		String theString = sc.nextLine();
		
		while (sc.hasNextLine()) {
			theString = theString + "\n" + sc.nextLine();
			
		}
		String[] aux = theString.split("\n");
		for(int i = aux.length-1; i > -1; i--){
			if(aux[i].contains("reta")){
				String x = aux[i].substring(aux[i].indexOf(':') + 1);
				int y = Integer.parseInt(x);
				log("reta: "+y);
				robot.Reta(-y,false);
				
				
			}
			if(aux[i].contains("curvardireita")){
				String raio = aux[i].substring(aux[i].indexOf(':') + 1, aux[i].indexOf(','));
				String angulo = aux[i].substring(aux[i].indexOf(',') + 1);
				int r = Integer.parseInt(raio);
				int a = Integer.parseInt(angulo);
				log("curvardireita: raio ="+r+" angulo ="+a);
				robot.CurvarEsquerda(r, a,false);
				
			}
			if(aux[i].contains("curvaresquerda")){
				String raio = aux[i].substring(aux[i].indexOf(':') + 1, aux[i].indexOf(','));
				String angulo = aux[i].substring(aux[i].indexOf(',') + 1);
				int r = Integer.parseInt(raio);
				int a = Integer.parseInt(angulo);
				log("curvaresquerda: raio ="+r+" angulo ="+a);
				robot.CurvarDireita(r, a,false);
				
			}
			if(aux[i].contains("parar")){
				String y = aux[i].substring(aux[i].indexOf(':') + 1);
				boolean x = Boolean.parseBoolean(y);
				log("STOP: "+x);
				robot.Parar(x);
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			System.out.println("valor de i: "+i);
			
		}
		this.robot.Parar(false);
		
		sc.close();
	}
	
	public void stopPlayer(){
		try {
			writerDir.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void doStop(){
		estado = estados.Stop;
	}
	public void doPlay(){
		estado = estados.Play;
	}
	public void doPlayInv(){
		estado = estados.PlayInverse;
	}
	
	
	@Override
	public void run() {
		while(estado != estados.ending){
			switch (estado) {
			case waiting:
				//log("Case: waiting");
				break;
			case Play:
				log("Case: Play");
				try {
					play();
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				estado = estados.waiting;
				break;
			case PlayInverse:
				log("Case: PlayInverse");
				try {
					playInverse();
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				estado = estados.waiting;
				break;
			case Stop:
				log("Case: Stop");
				stopPlayer();
				estado = estados.waiting;
				break;
			default:
				break;
			}
		}
	}
	
	
	

		

	
	

}

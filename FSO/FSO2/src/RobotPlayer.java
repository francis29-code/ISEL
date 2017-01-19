import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.util.Scanner;

public class RobotPlayer extends Thread implements ILogger{

	private MyRobot robot;
//	PrintWriter writerDir;
	Writer writerDir = null;
	File file;
	
	String url;
	estados estado;
	
	public enum estados{
		waiting,Play,PlayInverse,Stop,ending;
	}
	
	
	
	public RobotPlayer(MyRobot robot){
		this.robot = robot;
		url = "C:\\Users\\Diogo Fernandes\\workspace\\FSO2\\directions\\";
		file = new File(url+"directions.txt");
		
//		try {
//			writerDir= new PrintWriter(file);
//		} catch (FileNotFoundException e) {
//			// TODO Auto-generated catch blocks
//			e.printStackTrace();
//		}
		
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
				robot.Reta(y);
				
				
			}
			if(aux[i].contains("curvardireita")){
				String raio = aux[i].substring(aux[i].indexOf(':') + 1, aux[i].indexOf(','));
				String angulo = aux[i].substring(aux[i].indexOf(',') + 1);
				int r = Integer.parseInt(raio);
				int a = Integer.parseInt(angulo);
				log("curvardireita: raio ="+r+" angulo ="+a);
				robot.CurvarDireita(r, a);
				
			}
			if(aux[i].contains("curvaresquerda")){
				String raio = aux[i].substring(aux[i].indexOf(':') + 1, aux[i].indexOf(','));
				String angulo = aux[i].substring(aux[i].indexOf(',') + 1);
				int r = Integer.parseInt(raio);
				int a = Integer.parseInt(angulo);
				log("curvaresquerda: raio ="+r+" angulo ="+a);
				robot.CurvarEsquerda(r, a);
				
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
	
	public void playInverse(){
		
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
				log("Case: waiting");
				break;
			case Play:
				log("Case: Play");
				try {
					play();
				} catch (FileNotFoundException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;
			case PlayInverse:
				log("Case: PlayInverse");
				playInverse();
				break;
			case Stop:
				log("Case: Stop");
				stopPlayer();
				break;
			default:
				break;
			}
		}
	}
	
	
	
	public static void main(String args[]){
//		String url = "C:\\Users\\Diogo Fernandes\\workspace\\FSO - Copy\\directions\\";
//		File file = new File(url+"directions.txt");
//		try {
//			PrintWriter writerDir= new PrintWriter(file);
//			writerDir.println("asdfghjklç dfgk");
//			writerDir.println("asdfghjklç dfgk");
//			writerDir.println("asdfghjklç dfgk");
//			writerDir.println("asdfghjklç dfgk");
//			writerDir.println("asdfghjklç dfgk");
//			
//			
//		} catch (FileNotFoundException e) {
//			// TODO Auto-generated catch blocks
//			e.printStackTrace();
//		}
		
	}
		

	
	

}

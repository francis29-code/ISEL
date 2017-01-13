import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.Scanner;

public class RobotPlayer implements ILogger{

	private MyRobot robot;
	PrintWriter writerDir;
	File file;

	
	public RobotPlayer(MyRobot robot){
		this.robot = robot;
		file = new File("directions.txt");
		try {
			writerDir= new PrintWriter(file);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}
	
	public void recordDirections(String data){
		
		writerDir.write(data);
		
	    
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
				robot.Reta(y);
			}
			if(aux[i].contains("curvardireita")){
				String raio = aux[i].substring(aux[i].indexOf(':') + 1, aux[i].indexOf(','));
				String angulo = aux[i].substring(aux[i].indexOf(','));
				int r = Integer.parseInt(raio);
				int a = Integer.parseInt(angulo);
				robot.CurvarDireita(r, a);
			}
			if(aux[i].contains("curvaresquerda")){
				String raio = aux[i].substring(aux[i].indexOf(':') + 1, aux[i].indexOf(','));
				String angulo = aux[i].substring(aux[i].indexOf(','));
				int r = Integer.parseInt(raio);
				int a = Integer.parseInt(angulo);
				robot.CurvarEsquerda(r, a);
			}
			if(aux[i].contains("parar")){
				String y = aux[i].substring(aux[i].indexOf(':') + 1);
				boolean x = Boolean.parseBoolean(y);
				robot.Parar(x);
			}
		}
		
		sc.close();
	}
	
	public void playInverse(){
		
	}
	
	public void stopPlayer(){
		
	
	}
	
	
	
	
	
	
	public static void main(String args[]){
		
	}
	

}

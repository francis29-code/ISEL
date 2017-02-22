import java.util.ArrayList;

public class ThreadKeeper {
	
	private Thread th;
	private ArrayList<Thread> container;
	
	public ThreadKeeper() {
		this.container = new ArrayList<>();
		this.th = null;
		
	}
	
	public Thread getThread(String name){
		
		for(int i=0; i<container.size();i++){
			this.th = this.container.get(i);
			if(th.getName().compareTo(name)==0){
				return this.th;
			}
		}
		
		return null;
	}
	
	public void addThread(Thread thread){		
		this.container.add(thread);
	}
	
	public void priotirizeThread(String nome){
		Thread th = getThread(nome);
		this.container.add(0,th);
	}
	

}

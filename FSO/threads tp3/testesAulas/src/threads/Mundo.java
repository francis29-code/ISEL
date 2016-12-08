package threads;

import java.util.concurrent.Semaphore;

public class Mundo extends Thread{
	
	public Semaphore s1,s2;
	
	public Mundo(Semaphore s1, Semaphore s2){
		this.s1 = s1;
		this.s2 = s2;
	}
	
	public void run(){
		for(int i=0; i<5;i++){
			try {
				this.s1.acquire();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println("mundo");
			this.s2.release();
		}
	}
}

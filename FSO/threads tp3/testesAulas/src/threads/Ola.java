package threads;

import java.util.concurrent.Semaphore;

public class Ola extends Thread{
	
	public Semaphore s1,s2;
	
	public Ola(Semaphore s1, Semaphore s2){
		this.s1 = s1;
		this.s2 = s2;
	}
	
	public void run(){
		for(int i=0; i<5; i++){
			try {
				this.s2.acquire();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			System.out.println("ola");
			this.s1.release();
		}
	}
}

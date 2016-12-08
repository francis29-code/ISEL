package threads;

import java.util.concurrent.Semaphore;

public class LançaThreads {

	
	public static void main(String [] args) throws InterruptedException{
		Semaphore s1 = new Semaphore(0);
		Semaphore s2 = new Semaphore(1);
		
		Thread m = new Mundo(s1,s2);
		
		m.start();
		
		Thread.sleep(5000);
		
		Thread o = new Ola(s1,s2);
		
		o.start();
		//s2.realease()
		o.join();
		m.join();
	}
}

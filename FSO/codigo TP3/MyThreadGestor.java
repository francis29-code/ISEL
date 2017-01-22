import java.util.concurrent.Semaphore;

public class MyThreadGestor extends Thread implements Runnable, ILogger {

	private enum Estados {
		PAUSE, WAITING, END, RESUME, LSEGUIR
	};

	private Estados estados;
	private Semaphore sEspera, sAcesso;

	private MyThreadVaguear v;
	private MyThreadEvitar e;
	private MyThreadSeguir s;

	protected MyRobot theRobot;

	public MyThreadGestor(MyRobot theRobot, MyThreadVaguear v, MyThreadEvitar e, MyThreadSeguir s, Semaphore sAcesso) {
		this.sEspera = new Semaphore(0);
		this.sAcesso = sAcesso;
		this.estados = Estados.PAUSE;
		this.v = v;
		this.e = e;
		this.s = s;
		this.theRobot = theRobot;

	}

	public void myPause() {
		this.estados = Estados.PAUSE;
	}

	public void myResume() {
		if (sEspera.availablePermits() <= 0) {
			this.estados = Estados.RESUME;
			this.sEspera.release();

		}

	}

	public void myEnd() {
		this.estados = Estados.END;
		this.sEspera.release();
	}

	public void run() {

		while (estados != Estados.END) {
						
			switch (estados) {
			case END:
				break;
				
			case PAUSE:

				v.myPause();
				e.myPause();
				s.myPause();

				try {
					this.theRobot.theLogger.log("Gestor em pausa");
					this.sEspera.acquire();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;

			case RESUME:
				v.myResume();
				e.myWait();

				estados = Estados.WAITING;
				break;

			case WAITING:

				/* Teste sensor US WATING */

				try {

					this.sAcesso.acquire();

					if (this.theRobot.GetLowSpeedSensor() < 100) {
						/* Resumir Thread Seguir Parede */
						v.myPause();
						s.myResume();
						this.sAcesso.release();
						if (estados != Estados.PAUSE) {
							estados = Estados.LSEGUIR;
						}

					} else {
						
						if (estados != Estados.PAUSE) {
							estados = Estados.LSEGUIR;
						}

						this.sAcesso.release();
					}

				} catch (InterruptedException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}

				break;

			case LSEGUIR:

				try {
					sAcesso.acquire();

					if (this.theRobot.GetLowSpeedSensor() > 100) {
						sAcesso.release();
						s.myPause();

						if (estados != Estados.PAUSE) {
							estados = Estados.RESUME;
						}
					} else {
						sAcesso.release();
					}

				} catch (InterruptedException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}

				break;

			default:
				break;
			}
		}
		this.theRobot.theLogger.log("Gestor Terminou");
	}

	@Override
	public String log(String message, Object... args) {
		// TODO Auto-generated method stub
		return null;
	}

}
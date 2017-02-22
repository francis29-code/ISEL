import java.util.concurrent.Semaphore;

public class SegueParede extends Thread implements ILogger {

	private int distCtrl;

	private MyRobot robot;

	private Semaphore acessoRobot, ownSemaphore;

	private int oldDistance, newDistance, currentSleep, auxDistance;

	private States currentState;

	private boolean checked;

	private CaixaCorreio caixa;

	@Override
	public String log(String message, Object... args) {
		String aux1, aux2;
		aux1 = String.format( message, args );
		
		aux2 = String.format( "[%s] %s", this.getName(), aux1 );

		System.out.println( aux2 );

		return aux2;
	}

	public SegueParede(MyRobot robot, Semaphore semaphore, CaixaCorreio caixa) {
		this.setName("Segue");
		this.robot = robot;
		this.acessoRobot = semaphore;
		this.oldDistance = 0;
		this.newDistance = 0;
		this.distCtrl = 0;
		this.currentSleep = 0;
		this.auxDistance = 0;
		this.checked = false;
		this.currentState = States.Waiting;
		this.ownSemaphore = new Semaphore(0);
		this.caixa = caixa;
	}
	
	public States currentState(){
		return this.currentState;
	}

	public void myPause() {
		this.currentState = States.Waiting;
		this.robot.Parar(true);
	}


	public int getSleepTime() {
		return this.currentSleep = 20 * 5 / 100;
	}
	
	public boolean isChecked(){
		return this.checked;
	}

	public void updateCheck(boolean check) {
		this.checked = check;
		if (!this.checked) {
			myPause();
		} else {
			myResume();
		}
	}

	public void setNewDistance(int distanceRead) {
		this.oldDistance = this.newDistance;
		this.newDistance = distanceRead;
	}

	public void myResume() {
		this.ownSemaphore.release();
		this.currentState = States.Reading;
	}

	private double getCurveDistance(double angle, double radius) {
		double perimeter = 2.0 * Math.PI * radius;
		return angle * perimeter / 360.0;
	}

	private double getSleepTime(double distance) {
		double sleepTime;
		sleepTime = distance * 5.0 / 100.0;

		this.log("getSleepTime(%3.2f)->%3.2f", distance, sleepTime);

		return sleepTime;
	}

	private double getSleepTime(double angle, double radius) {
		return getSleepTime(getCurveDistance(angle, radius));
	}


	private void myAction() {
		double radAngle = ((double) this.oldDistance - (double) this.newDistance) / (double) this.distCtrl;
		double radianos = Math.atan(radAngle);
		double degrees = (radianos * 360) / (2 * Math.PI);
		this.log("--------------------------------- angulo calculado: " + degrees);
		if (degrees > 3 || degrees < -3) {
			if (this.oldDistance > this.newDistance) {
				this.robot.CurvarEsquerda(0, (int) degrees);
				this.robot.Parar(false);
				this.acessoRobot.release();
				try {
					Thread.sleep((int) getSleepTime((int) degrees, 0) * 1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			} else {
				this.robot.CurvarDireita(0, (int) degrees);
				this.robot.Parar(false);
				this.acessoRobot.release();
				try {
					Thread.sleep((int) getSleepTime((int) degrees, 0) * 1000);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			if (this.currentState != States.Waiting) {
				this.currentState = States.ReadingV2;
			}
		} else {
			if (this.currentState != States.Waiting) {
				this.currentState = States.Control;
			}
		}
	}

	private void myReading() throws Exception{
		auxDistance = (Integer)caixa.removerElemento();
		this.log("LI Primeira DISTANCIA: " + auxDistance);

		if (auxDistance < 100 && auxDistance > 20) {
			try {
				this.acessoRobot.acquire();
				setNewDistance(auxDistance);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			if (this.currentState != States.Waiting) {
				this.currentState = States.Control;
			}

		} else {
			if (this.currentState != States.Waiting) {
				this.currentState = States.Reading;
			}

			try {
				Thread.sleep(500);
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		}
	}

	private void myControl() {
		this.robot.Reta(20);
		this.robot.Parar(false);
		this.acessoRobot.release();
		try {
			Thread.sleep(getSleepTime() * 1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (this.currentState != States.Waiting) {
			this.currentState = States.ReadingV2;
		}

	}

	private void myReadingV2() throws Exception{
		auxDistance = (Integer)caixa.removerElemento();
		this.log("LI Segunda DISTANCIA: " + auxDistance );

		if (auxDistance < 100 && auxDistance > 20) {
			try {
				this.acessoRobot.acquire();
				setNewDistance(auxDistance);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			if (this.currentState != States.Waiting) {
				this.currentState = States.Turn;

			}
		} else {
			if (this.currentState != States.Waiting) {
				this.currentState = States.ReadingV2;
			}
			try {
				Thread.sleep(500);
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
		}
	}

	@Override
	public void run() {
		while (this.currentState != States.Ending) {
			switch (this.currentState) {
			case Waiting:
				this.log("ESTOU NO WAITING DO SEGUEPAREDE");
				this.log("ESTADO A PRINTAR " + this.currentState);
				try {
					this.ownSemaphore.acquire();
				} catch (Exception e) {
					e.printStackTrace();
				}
				break;

			case Reading:
				this.log("ESTADO A PRINTAR " + this.currentState);
				try {
					myReading();
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;

			case Control:
				this.log("ESTADO A PRINTAR " + this.currentState);
				myControl();
				break;
			//
			case ReadingV2:
				this.log("ESTADO A PRINTAR " + this.currentState);
				try {
					myReadingV2();
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				break;

			case Turn:
				this.log("ESTADO A PRINTAR " + this.currentState);
				myAction();
				break;

			default:
				break;
			}
		}
	}

}

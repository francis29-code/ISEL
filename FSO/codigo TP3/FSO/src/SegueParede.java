
public class SegueParede extends Thread implements ILogger {

	private MyRobot robot;

	private enum States {
		Waiting, Running, Reading, Ending
	}

	private States currentState;

	@Override
	public String log(String message, Object... args) {
		String aux;
		aux = String.format(message, args);

		System.out.println(aux);

		return aux;
	}

	public SegueParede(MyRobot robot) {
		// TODO Auto-generated constructor stub
		this.robot = robot;
		this.currentState = States.Waiting;
	}

	public void myPause() {
		this.currentState = States.Waiting;
	}

	public void myResume() {
		this.currentState = States.Running;
	}

	public void myEnding() {
		this.currentState = States.Ending;
	}

	@Override
	public void run() {
		while (this.currentState != States.Ending) {
			switch (this.currentState) {
			case Waiting:

				break;

			case Running:

				break;

			case Reading:

				break;

			default:
				break;
			}

		}

	}

}

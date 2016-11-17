
public class AvoidObstacle implements ILogger { 
	final int MAX_DISTANCE = 70;
	
	final int MAX_ANGLE = 90;
	
	final int MAX_RADIUS = 0;
	
	protected String robotName;
	
	protected MyRobot theRobot;
	
	@Override
	public String log(String message, Object... args) {
    String aux;
    aux = String.format(message, args);
    
    System.out.println( aux );
    
    return aux;
  }
	
	public AvoidObstacle(String name, boolean simulateRobot) {
		this.robotName = name;
		
		this.theRobot = new MyRobot( simulateRobot, this );
		
		if ( this.theRobot.OpenNXT( this.robotName )==false ) {
		  String message;
		  message = this.log( "Could not connect to robot %s", this.robotName );
			
			throw new IllegalArgumentException( message );
		}
		
		this.theRobot.SetSpeed(50);
		

	}
	private int getCurveDistance(double angle, double radius) {
		double perimeter = 2.0 * Math.PI * radius;
		return (int) (angle * perimeter / 360.0);
	}
	
	
	public void doAvoidObstacle(){
		this.theRobot.Reta(-MAX_DISTANCE);
//		this.log("backwards(%3.2d)", MAX_DISTANCE);
		this.theRobot.CurvarDireita(MAX_RADIUS, MAX_ANGLE);
//		this.log("Right(%3.2d, %3.2d)->%3.2d", MAX_RADIUS, MAX_ANGLE, getCurveDistance(MAX_RADIUS, MAX_ANGLE) );
		this.theRobot.CloseNXT();
	}
	
	
}

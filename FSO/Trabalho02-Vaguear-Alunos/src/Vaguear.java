import java.util.Random;

public class Vaguear implements ILogger {
	public final int MinForward = 50;  // Centimeters
	public final int RndForward = 40;  // Centimeters
	
	public final int MinRadius = 50;   // Centimeters
	public final int RndRadius = 30;   // Centimeters
	
	public final int MinAngle = 30;    // Degrees
	public final int RndAngle = 60;    // Degrees
	
	public final int SensorSleepTime = 250;  // Milliseconds
	
	public enum Directions {Stop, Right, Left, Forward };
	
	public Directions currentDirection;
	
	protected String robotName;
	
	protected Random rnd;
	
	protected MyRobot theRobot;
	
	@Override
	public String log(String message, Object... args) {
    String aux;
    aux = String.format(message, args);
    
    System.out.println( aux );
    
    return aux;
  }
	
	public Vaguear(String name, int touchSensor, boolean simulateRobot) {
		this.robotName = name;
		this.currentDirection = Directions.Stop;
		
		this.rnd = new Random();
		
		this.theRobot = new MyRobot( simulateRobot, this );
		
		if ( this.theRobot.OpenNXT( this.robotName )==false ) {
		  String message;
		  message = this.log( "Could not connect to robot %s", this.robotName );
			
			throw new IllegalArgumentException( message );
		}
		
		this.theRobot.SetSpeed( 50 );
		this.theRobot.SetTouchSensor( touchSensor );
	}
	
	private Directions getNextDirection() {
		int aux;
		aux = this.rnd.nextInt( 90 );
			
		if ( aux<30 ) {
			return Directions.Right;
		}

		if ( aux<60 ) {
		  return Directions.Left;
		}
		
		return Directions.Forward;
	}
	
	private int getRandomRadius() {
		return this.MinRadius + this.rnd.nextInt( this.RndRadius );
	}
	
	private int getRandomAngle() {
		return this.MinAngle + this.rnd.nextInt( this.RndAngle );
	}
	
	private int getRandomDistance() {
		return this.MinForward + this.rnd.nextInt( this.RndForward );
	}
	
	private double getCurveDistance(double angle, double radius) {
		double perimeter = 2.0 * Math.PI * radius;
		return angle * perimeter / 360.0;
	}
	
	/**
	 * In average if the robot speed is 50% it takes approximately 5 seconds
	 * to travel 100 centimeters (1 meter).
	 * 
	 * This method should be changed to work with "different speeds"
	 */
	private double getSleepTime(double distance) {
		double sleepTime;
		sleepTime = distance * 5.0 / 100.0;
		
		this.log( "getSleepTime(%3.2f)->%3.2f", distance, sleepTime);
		
		return sleepTime;
	}
	
	private double getSleepTime(double angle, double radius) { 
		return getSleepTime ( getCurveDistance(angle, radius) );
	}
	
	private boolean waitForDistanceAndTestSensor(int sleepTime) throws Exception {
	  
	  this.log( "Waiting %d miliseconds...", sleepTime );
	  Thread.sleep( sleepTime );
	  return this.theRobot.GetTouchSensor()==true;
	}
	
	public void doWork() throws Exception {
		boolean work;
		work = true;
		
		double radius, angle, distance;
		
		double sleepTime=0.0;
		
		for( ; work==true ; ) {
			Directions newDirection;
			
			while ( (newDirection=getNextDirection())==this.currentDirection )
				;
			
			this.currentDirection = newDirection;
			
			switch ( this.currentDirection ) {
				case Right:
					radius = getRandomRadius();
					angle = getRandomAngle();
					sleepTime = getSleepTime( radius, angle );
					this.theRobot.CurvarDireita( (int)radius, (int)angle);
					this.log( "Right(%3.2f, %3.2f)->%3.2f", radius, angle, getCurveDistance(radius, angle) );
					break;
				case Forward:
					distance = getRandomDistance();
					sleepTime = getSleepTime( distance );
					this.theRobot.Reta( (int)distance );
					this.log( "Forward(%3.2f)", distance );
					break;
				case Left:
					radius = getRandomRadius();
					angle = getRandomAngle();
					sleepTime = getSleepTime( radius, angle );
					this.theRobot.CurvarEsquerda( (int)radius, (int)angle);
					this.log( "Left(%3.2f, %3.2f)->%3.2f", radius, angle, getCurveDistance(radius, angle) );
					break;
				default:
					break;
			}
			// Uncomment next line to force a stop after each movement
			//this.theRobot.Parar( false );
			
			this.log( "Sleep(%3.2f)", sleepTime );
			
			if ( this.waitForDistanceAndTestSensor( (int)(sleepTime * 1000.0) )==true ) {
			  this.theRobot.Parar( true );
			  this.log( "Colision" );
			  work = false;
			}
		}
		
		this.theRobot.CloseNXT();
	}
}
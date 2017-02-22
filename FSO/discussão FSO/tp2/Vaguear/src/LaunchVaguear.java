public class LaunchVaguear {
	
	public static void main(String[] args) throws Exception {
		
	  try {
  		String robotName;
  		robotName = args[0];
  		
  		int touchSensorPort;
  		if ( args.length>1 ) {
  		  touchSensorPort = Integer.parseInt( args[1] );
  		}
  		else {
  		  touchSensorPort = MyRobot.Sensor2;
  		}
  		
  		boolean simulateRobot;
  		if ( args.length>2 ) {
  		  simulateRobot = Boolean.parseBoolean( args[2] );
  		}
  		else {
  		  simulateRobot = true;
  		}
  		
  		Vaguear v;
  		v = new Vaguear( robotName, touchSensorPort, simulateRobot , false);
  		v.readMailBox();
  		System.exit( 0 );
  		
	  }
	  catch (Exception ex) {
	    System.out.println( "Usage:" );
	    System.out.println( "java " + LaunchVaguear.class.getCanonicalName() + " [RobotName] <touch sensor port> <simulate flag (true/false)>" );
	    System.exit( 1 );
	  }
	}
}

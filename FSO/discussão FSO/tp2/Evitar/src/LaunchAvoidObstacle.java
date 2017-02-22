public class LaunchAvoidObstacle{
	
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

  		
  		AvoidObstacle ao;
  		ao = new AvoidObstacle( robotName, touchSensorPort, simulateRobot, false );
  		ao.readMailBox();
  		System.exit( 0 );
  		
	  }
	  catch (Exception ex) {
		ex.printStackTrace();
	    System.out.println( "Usage:" );
	    System.out.println( "java " + LaunchAvoidObstacle.class.getCanonicalName() + " <simulate flag (true/false)>" );
	    System.exit( 1 );
	  }
	}
	
	
}

public class LaunchAvoidObstacle {
	
	public static void main(String[] args) throws Exception {
		
	  try {
  		String robotName;
  		robotName = args[0];
  		
  		boolean simulateRobot;
  		if ( args.length>1 ) {
  		  simulateRobot = Boolean.parseBoolean( args[1] );
  		}
  		else {
  		  simulateRobot = true;
  		}
  		
  		AvoidObstacle ao;
  		ao = new AvoidObstacle( robotName, simulateRobot );
  		ao.doAvoidObstacle();
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

import java.util.Random;

public class MyRobot {
  public static final int Sensor1 = RobotLego.S_1;
  
  public static final int Sensor2 = RobotLego.S_2;
  
  public static final int Sensor3 = RobotLego.S_3;
  
  public static final int Sensor4 = RobotLego.S_4;
  
  private final int SensorMessageTime = 50; // Milliseconds
  
	private RobotLego robot;
	
	protected int touchSensor;
	
	protected int sensorUS;
	
	private final boolean simulateRobot;
	
	private final Random rnd;
	
	private final ILogger theLogger;
	
	public MyRobot(boolean simulateRobot, ILogger theLogger) {
		this.simulateRobot = simulateRobot;
		this.rnd = new Random();
		this.theLogger = theLogger;
		
		if ( this.simulateRobot==false ) {
		  this.robot = new RobotLego();
		}
		else {
		  this.robot = null;
		}
	}
	
	public boolean OpenNXT(String nome) {
		if ( this.simulateRobot==false) {
			return this.robot.OpenNXT( nome );
		}
		this.theLogger.log( "OpenNXT(%s)", nome );
		
		return true;
	}
	
	public void CloseNXT() {
		if ( this.simulateRobot==false) {
			this.robot.CloseNXT();
		}
		else {
		  this.theLogger.log( "CloseNXT()" );
		}
	}
	
	public void Parar(boolean b) {
		if ( this.simulateRobot==false) {
			this.robot.Parar(b);
		}
		else {
			this.theLogger.log( "Parar(%b)", b );
		}
	}
	
	public void Reta(int distancia) {
		if ( this.simulateRobot==false) {
			this.robot.Reta( distancia );
		}
		else {
			this.theLogger.log( "Reta(distancia->%d)", distancia );
		}
	}
	
	public void CurvarEsquerda(int raio, int angulo) {
		if ( this.simulateRobot==false) {
			this.robot.CurvarEsquerda(raio, angulo);
		}
		else {
			this.theLogger.log( "CurvarEsquerda(raio->%d, angulo->%d)", raio, angulo );
		}
	}
	
	public void CurvarDireita(int raio, int angulo) {
		if ( this.simulateRobot==false) {
			this.robot.CurvarDireita(raio, angulo);
		}
		else {
			this.theLogger.log( "CurvarDireita(raio->%d, angulo->%d)", raio, angulo );
		}
	}
	
	public void AjustarVME(int offSet) {
		if ( this.simulateRobot==false) {
			this.robot.AjustarVME( offSet );
		}
		else {
			this.theLogger.log( "AjustarVME(offSet->%d)", offSet );
		}
	}
	
	public void AjustarVMD(int offSet) {
		if ( this.simulateRobot==false) {
			this.robot.AjustarVMD( offSet );
		}
		else {
			this.theLogger.log( "AjustarVMD(offSet->%d)", offSet );
		}
	}
	
	public void SetSpeed(int speed) {
		if ( this.simulateRobot==false) {
			this.robot.SetSpeed( speed);
		}
		else {
			this.theLogger.log( "SetSpeed(speed->%d)", speed);
		}
	}
	
	public void SetTouchSensor(int touchSensor) {
	  this.touchSensor = touchSensor;
	  
    if ( this.simulateRobot==false) {
      this.robot.SetSensorTouch( this.touchSensor );
    }
    else {
      this.theLogger.log( "SetTouchSensor(touchSensor->%d)", this.touchSensor );
    }
  }
	
	public void SetSensorLowSpeed(int sensorUS){
		this.sensorUS = sensorUS;
		if ( this.simulateRobot==false) {
		      this.robot.SetSensorLowspeed(this.sensorUS);
		    }
		    else {
		      this.theLogger.log( "SetSensorUS(sensorUS->%d)", this.sensorUS );
		    }
	}
	
	public boolean GetTouchSensor() {
    if ( this.simulateRobot==false) {
      return this.robot.Sensor( this.touchSensor )==1;
    }
    else {
      this.theLogger.log( "GetTouchSensord()" );
      return this.rnd.nextInt(1000)>900;
    }
  }
	
	public int GetSensorUS(){
	    if ( this.simulateRobot==false) {
	        return this.robot.SensorUS(this.sensorUS);
	      }
	      else {
	        this.theLogger.log( "GetSensorUS()" );
	        return this.rnd.nextInt(2555)/10;
	      }
	}
	
	public int GetSensorDelay() {
	  if ( this.simulateRobot==false) {
      return SensorMessageTime;
    }
	  else {
	    return 0;
	  }
	}
	
	
	
	public static void main(String[] args){
		Random rnd;
		rnd = new Random();
		int a =0;
		for(int i=0;i<7;i++){
			a = rnd.nextInt(2555)/10;
			System.out.println("numero "+i+": "+a+"\n");
		}
		
		
	}
	
}

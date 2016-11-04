package TP;

import RobotLego.RobotLego;

public class Vaguear {
	
	private RobotLego robot;
	private Paths path;
	
	public enum Paths{
		right,left,forward,backward,def;
	
		public Paths devolvedir(int i){
			 if(i < 3){
				 return Paths.forward;
			 }
			 if(i == 3){
				 return Paths.left;
			 }
			 if(i > 3){
				 return Paths.right;
			 }
			return Paths.def;
		}
	}
		
	private void doWander(){
		
		double radius = Math.random()*50;
		double angle = Math.random()*90;
		double distance = Math.random()*50;
		double pathSelector = Math.random()*4;
		
		path = path.devolvedir((int) pathSelector);
		
		switch (path) {
		case left:
			robot.Parar(true);
			robot.CurvarEsquerda((int) radius,(int) angle);
			doWander();
		case right:
			robot.Parar(true);
			robot.CurvarDireita((int) radius,(int) angle);
			doWander();
		case forward:
			robot.Parar(true);
			robot.Reta((int) distance);
			doWander();
		case backward:
			break;
		case def:
			doWander();
		}
	}
	
	public Vaguear(RobotLego robot){
		this.robot = robot;
		path = Paths.def;
		run();
	}
	
	public void run(){
		doWander();
	}

}

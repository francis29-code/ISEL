package prof;


import modProb.Problema;
import pee.Solucao;

public class ProcuraProfIter extends ProcuraProf{
	
	//quanto menos for o incremento melhor a solucao
	private int incProf = 1;
	
	public int getIncProf(){
		
		return incProf;
	}
	
	public void setIncProf(int incProf){
		this.incProf = incProf;
	}
	
	private Solucao resolver(Problema problema, int profMax, int incProf){
		
		for(int profMaxIt = incProf; profMaxIt<=profMax; profMaxIt+=incProf){
			Solucao solucao = super.resolver(problema,profMax);
			if(solucao != null){
				return solucao;
			}
		}
		return null;
	}
	
	@Override
	public Solucao resolver(Problema problema, int profMax){
		return resolver(problema,profMax,incProf);
	}
	

}

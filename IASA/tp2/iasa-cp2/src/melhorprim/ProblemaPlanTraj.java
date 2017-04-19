package melhorprim;

import modProb.Estado;
import modProb.Problema;

public class ProblemaPlanTraj extends Problema{
	
	private EstadoLocalidade estadoFinal;

	public ProblemaPlanTraj(String locini, String locfin, OperadorPuzzle[] operadores) {
		super(new EstadoLocalidade(locini),operadores);
		estadoFinal = new EstadoLocalidade(locfin);
	}
	
	@Override
	public boolean objectivo(Estado estado) {
		if(estado.equals(estadoFinal)){
			return true;
		}
		return false;
	}

}

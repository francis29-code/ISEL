package pee;

import pee.modProb.Estado;
import pee.modProb.Operador;

public interface PassoSolucao {

	
	Estado getEstado();
	
	Operador getOperador();
	
	double getCusto();
}

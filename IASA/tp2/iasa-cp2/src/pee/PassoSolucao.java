package pee;

import modProb.Estado;
import modProb.Operador;

public interface PassoSolucao {

	
	Estado getEstado();
	
	Operador getOperador();
	
	double getCusto();
}

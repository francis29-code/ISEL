package pee;

import pee.modProb.Problema;

public interface Procura {
	
	Solucao resolver(Problema problema);
	
	Solucao resolver(Problema problema, int profMax);
}

package pee;

import modProb.ProblemaHeur;

public interface ProcuraHeur {
	
	Solucao resolver(ProblemaHeur problema);
	
	Solucao resolver(ProblemaHeur problema, int profMax);
}

package pee.melhorprim;

import pee.mecproc.No;
import pee.modProb.ProblemaHeur;

public class ProcuraSofrega extends ProcuraMelhorPrim<ProblemaHeur> implements ProcuraHeur{

	@Override
	protected double f(No no) {
		//apenas usa o motor da heuristica
		//f(n) = h(n)
		return problema.heuristica(no.getEstado());
	}

}

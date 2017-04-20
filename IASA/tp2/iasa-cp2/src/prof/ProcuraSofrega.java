package prof;

import mem.No;
import mem.ProcuraMelhorPrim;
import modProb.ProblemaHeur;
import pee.ProcuraHeur;

public class ProcuraSofrega extends ProcuraMelhorPrim<ProblemaHeur> implements ProcuraHeur{

	@Override
	protected double f(No no) {
		//apenas usa o motor da heuristica
		//f(n) = h(n)
		return problema.heuristica(no.getEstado());
	}

}

package prof;

import mem.No;
import mem.ProcuraMelhorPrim;
import modProb.ProblemaHeur;
import pee.ProcuraHeur;

public class ProcuraAA extends ProcuraMelhorPrim<ProblemaHeur> implements ProcuraHeur{

	@Override
	protected double f(No no) {
		//utiliza o custo e a heuristica das diferentes procuras
		//f(n) = h(n)+g(n)
		return problema.heuristica(no.getEstado()) + no.getCusto();
	}

}

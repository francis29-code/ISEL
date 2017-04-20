package prof;

import mem.No;
import mem.ProcuraMelhorPrim;
import modProb.Problema;
import pee.Procura;


public class ProcuraCustoUnif extends ProcuraMelhorPrim<Problema> implements Procura {

	@Override
	protected double f(No no) {
		//f(n) = g(n)
		//sendo que g(n) apenas usa o CUSTO
		return no.getCusto();
		
	}
	
	

}

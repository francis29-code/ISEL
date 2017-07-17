package pee.melhorprim;

import pee.Procura;
import pee.mecproc.No;
import pee.modProb.Problema;


public class ProcuraCustoUnif extends ProcuraMelhorPrim<Problema> implements Procura {

	@Override
	protected double f(No no) {
		//f(n) = g(n)
		//sendo que g(n) apenas usa o CUSTO
		return no.getCusto();
		
	}
	
	

}

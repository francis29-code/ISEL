package prof;

import mem.No;
import mem.ProcuraMelhorPrim;
import modProb.Problema;
import pee.Procura;


public class ProcuraCustoUnif extends ProcuraMelhorPrim<Problema> implements Procura {

//	@Override
//	public Solucao resolver(Problema problema) {
//	
//		return null;
//	}
//
//	@Override
//	public Solucao resolver(Problema problema, int profMax) {
//		return null;
//	}

	@Override
	protected double f(No no) {
		return no.getCusto();
		
	}
	
	

}

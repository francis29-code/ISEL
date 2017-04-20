package mem;

import java.util.Comparator;
import mecproc.MecanismoProcura;
import modProb.Problema;

public abstract class ProcuraMelhorPrim<P extends Problema> 
				extends MecanismoProcura<P> 
				implements Comparator<No>{
	
	@Override
	protected MemoriaProcura iniciarMemoria(){
		return new MemoriaPrioridade(this);
	}
	
	@Override
	public int compare(No o1, No o2){
		/*
		 * 1 - quando o1 maior que o2
		 * 0 - quando o1 igual a o2
		 * -1 - quando o1 menor o2
		 */
		return Double.compare(f(o1), f(o2));
	}
	
	
	protected abstract double f(No no);
}

package prof;

import mecproc.MecanismoProcura;
import mem.MemoriaLIFO;
import mem.MemoriaProcura;
import modProb.Problema;

public class ProcuraProf extends MecanismoProcura<Problema>{

	@Override
	protected MemoriaProcura iniciarMemoria() {
		// TODO Auto-generated method stub
		return new MemoriaLIFO();
	}

}

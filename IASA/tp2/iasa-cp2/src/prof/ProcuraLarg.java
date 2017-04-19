package prof;

import mecproc.MecanismoProcura;
import mem.MemoriaFIFO;
import mem.MemoriaProcura;
import modProb.Problema;

public class ProcuraLarg extends MecanismoProcura<Problema> {

	@Override
	protected MemoriaProcura iniciarMemoria() {
		// TODO Auto-generated method stub
		return new MemoriaFIFO();
	}

}

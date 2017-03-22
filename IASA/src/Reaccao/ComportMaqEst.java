package Reaccao;

import java.util.HashMap;
import java.util.Map;

import Maqest.Estado;
import Maqest.MaquinaEstados;

public abstract class ComportMaqEst implements Comportamento {
	
	private MaquinaEstados<Estimulo> maqEst;
	private Map<Estado,Comportamento> comportamentos;
	
	public ComportMaqEst() {
		comportamentos = new HashMap<Estado,Comportamento>();
		maqEst = iniciar();
	}

	@Override
	public Accao ativar(Estimulo estimulo) {
		
		Comportamento comport = comportamentos.get(maqEst.getEstado());
		Accao accao = (comport != null ? comport.ativar(estimulo) : null );
		
		maqEst.processarEvento(estimulo);
		
		return accao;
	}

	public Estado<Estimulo> getEstado() {
		return maqEst.getEstado();
	}

	public ComportMaqEst comport(Estado<Estimulo> estado, Comportamento comport) {
		comportamentos.put(estado, comport);
		return this;
	}

	protected abstract MaquinaEstados<Estimulo> iniciar();
}

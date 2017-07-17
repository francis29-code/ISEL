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
		
		//verifica��o da ac��o a retornar, de acordo com o estimulo obtido do ambiente
		
		Comportamento comport = comportamentos.get(maqEst.getEstado());
		Accao accao = (comport != null ? comport.ativar(estimulo) : null );
		
		maqEst.processarEvento(estimulo);
		
		return accao;
	}

	public Estado<Estimulo> getEstado() {
		//estado atual da m�quina de estados
		return maqEst.getEstado();
	}

	public ComportMaqEst comport(Estado<Estimulo> estado, Comportamento comport) {
		//adiciona-se ao mapa os comportamentos da m�quina de estados
		// provenientes do ComportamentoPersonagem e do m�todo iniciar(), que ganha corpo na classe anteriormente definida
		comportamentos.put(estado, comport);
		return this;
	}

	protected abstract MaquinaEstados<Estimulo> iniciar();
}

package Reaccao;

public class Reaccao implements Comportamento {
	
	private Estimulo estimulo;
	private Accao accao;
	
	public Reaccao(Estimulo estimulo, Accao accao) {
		this.estimulo = estimulo;
		this.accao = accao;
	}

	@Override
	public Accao ativar(Estimulo estimulo) {
		return estimulo == this.estimulo ? accao : null;
	}
}

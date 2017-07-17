package Reaccao;

public class ComportHierarq implements Comportamento {
	
	private Comportamento[] comportamentos;
	
	public ComportHierarq(Comportamento[] comportamentos) {
		//comportamentos correspondentes �s reac��es em cada estado, que desencandeiam a��es
		this.comportamentos = comportamentos;
	}

	@Override
	public Accao ativar(Estimulo estimulo) {
		for(Comportamento comportamento : comportamentos){
			//se o estimulo de entrada corresponder a alguma accao possivel da rec�ao passada como parametro no construtor
			// retorna a accao devida
			Accao accao = comportamento.ativar(estimulo);
			if(accao != null){
				return accao;
			}
		}
		return null;
	}

}

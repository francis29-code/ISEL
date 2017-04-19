package Reaccao;

public class ComportHierarq implements Comportamento {
	
	private Comportamento[] comportamentos;
	
	public ComportHierarq(Comportamento[] comportamentos) {
		this.comportamentos = comportamentos;
	}

	@Override
	public Accao ativar(Estimulo estimulo) {
		for(Comportamento comportamento : comportamentos){
			Accao accao = comportamento.ativar(estimulo);
			if(accao != null){
				return accao;
			}
		}
		return null;
	}

}

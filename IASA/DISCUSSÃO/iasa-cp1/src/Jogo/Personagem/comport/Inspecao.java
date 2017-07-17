package Jogo.Personagem.comport;

import Jogo.Ambiente.AccaoAmb;
import Jogo.Ambiente.EventoAmb;
import Reaccao.ComportHierarq;
import Reaccao.Comportamento;
import Reaccao.Reaccao;

public class Inspecao extends ComportHierarq {
	public Inspecao(){
		super(new Comportamento[]{
				new Reaccao(EventoAmb.INIMIGO, AccaoAmb.APROXIMAR),
				new Reaccao(EventoAmb.RUIDO, AccaoAmb.PROCURAR)
		});
	}
}

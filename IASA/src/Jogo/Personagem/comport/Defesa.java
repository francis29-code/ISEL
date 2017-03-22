package Jogo.Personagem.comport;

import Jogo.Ambiente.AccaoAmb;
import Jogo.Ambiente.EventoAmb;
import Reaccao.ComportHierarq;
import Reaccao.Comportamento;
import Reaccao.Reaccao;

public class Defesa extends ComportHierarq {

	public Defesa(){
		super(new Comportamento[]{
				new Reaccao(EventoAmb.INIMIGO,AccaoAmb.DEFENDER),
		});
	}
}

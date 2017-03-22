package Jogo.Personagem.comport;

import Jogo.Ambiente.AccaoAmb;
import Jogo.Ambiente.EventoAmb;
import Reaccao.ComportHierarq;
import Reaccao.Comportamento;
import Reaccao.Reaccao;

public class Combate extends ComportHierarq{
	
	public Combate(){
		super(new Comportamento[]{
				new Reaccao(EventoAmb.DERROTA,AccaoAmb.INICIAR),
				new Reaccao(EventoAmb.INIMIGO, AccaoAmb.ATACAR)
		});
	}
}

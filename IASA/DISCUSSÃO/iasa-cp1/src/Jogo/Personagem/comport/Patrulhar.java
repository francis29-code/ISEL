package Jogo.Personagem.comport;

import Jogo.Ambiente.AccaoAmb;
import Jogo.Ambiente.EventoAmb;
import Reaccao.ComportHierarq;
import Reaccao.Comportamento;
import Reaccao.Reaccao;

public class Patrulhar extends ComportHierarq{
	
	public Patrulhar(){
		super(new Comportamento[]{
				new Reaccao(EventoAmb.SILENCIO, AccaoAmb.PATRULHAR),
				new Reaccao(EventoAmb.INIMIGO, AccaoAmb.APROXIMAR),
				new Reaccao(EventoAmb.RUIDO, AccaoAmb.APROXIMAR)
		});
	}
}

package Jogo.Personagem.comport;

import Jogo.Ambiente.EventoAmb;
import Maqest.Estado;
import Maqest.MaquinaEstados;
import Reaccao.ComportMaqEst;
import Reaccao.Estimulo;

public class ComportPersonagem extends ComportMaqEst{

	@Override
	protected MaquinaEstados<Estimulo> iniciar(){
		//cria��o do espa�o de estados da personagem 
		Estado<Estimulo> patrulha = new Estado<Estimulo>("Patrulha");
		Estado<Estimulo> defesa = new Estado<Estimulo>("Defesa");
		Estado<Estimulo> combate = new Estado<Estimulo>("Combate");
		Estado<Estimulo> inspecao = new Estado<Estimulo>("Inspecao");
		
		patrulha
			.trans(EventoAmb.INIMIGO, defesa)
			.trans(EventoAmb.RUIDO, inspecao);
		inspecao
			.trans(EventoAmb.INIMIGO, defesa)
			.trans(EventoAmb.SILENCIO, patrulha);
		combate
			.trans(EventoAmb.FUGA, patrulha)
			.trans(EventoAmb.VITORIA, patrulha)
			.trans(EventoAmb.DERROTA, patrulha);
		defesa
			.trans(EventoAmb.INIMIGO, combate)
			.trans(EventoAmb.FUGA, inspecao);
		
		//definica��o dos estados e suas rea��es, rea��es que definem as ac��es aplicar de acordo com os estimulos
		comport(patrulha, new Patrulhar());
		comport(inspecao, new Inspecao());//inspecao
		comport(combate, new Combate());//combate
		comport(defesa, new Defesa());//defesa
		
		//retorna uma m�quina de estado, com os comportamentos definidos para cada estado
		//e o estado inicial da mesma, neste caso � patrulhar
		
		return new MaquinaEstados<Estimulo>(patrulha);
	}
}

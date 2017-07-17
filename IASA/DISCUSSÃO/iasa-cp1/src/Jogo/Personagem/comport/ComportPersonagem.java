package Jogo.Personagem.comport;

import Jogo.Ambiente.EventoAmb;
import Maqest.Estado;
import Maqest.MaquinaEstados;
import Reaccao.ComportMaqEst;
import Reaccao.Estimulo;

public class ComportPersonagem extends ComportMaqEst{

	@Override
	protected MaquinaEstados<Estimulo> iniciar(){
		//criação do espaço de estados da personagem 
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
		
		//definicação dos estados e suas reações, reações que definem as acções aplicar de acordo com os estimulos
		comport(patrulha, new Patrulhar());
		comport(inspecao, new Inspecao());//inspecao
		comport(combate, new Combate());//combate
		comport(defesa, new Defesa());//defesa
		
		//retorna uma máquina de estado, com os comportamentos definidos para cada estado
		//e o estado inicial da mesma, neste caso é patrulhar
		
		return new MaquinaEstados<Estimulo>(patrulha);
	}
}

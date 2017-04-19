package Jogo.Personagem;

import Jogo.Ambiente.Ambiente;
import Jogo.Personagem.comport.ComportPersonagem;
import Reaccao.Accao;
import Reaccao.Estimulo;

public class Personagem {
	private Ambiente ambiente;
	private ComportPersonagem comport;
	
	public Personagem(Ambiente ambiente){
		this.ambiente = ambiente;
		comport = new ComportPersonagem();
	}
	
	public void executar(){
		Estimulo estimulo = percepcionar();
		Accao accao = processar(estimulo);
		actuar(accao);
		mostrar();
	}
	
	private Estimulo percepcionar(){
		//estimulo é um evento
		return ambiente.obterEvento();
	}
	
	private Accao processar(Estimulo estimulo){
		//é uma accao amb
		Accao accao = comport.ativar(estimulo);
		return accao;
	}
	
	private void actuar(Accao accao){
		if(accao != null){
			accao.executar();
		}
	}
	
	private void mostrar(){
		System.out.printf("Estado: %s\n",comport.getEstado());
	}
}

package Jogo;

import Jogo.Ambiente.Ambiente;
import Jogo.Ambiente.EventoAmb;
import Jogo.Personagem.Personagem;

public class Jogo {
	private static Ambiente ambiente = new Ambiente();
	private static Personagem personagem = new Personagem(ambiente);
	
	private static void executarJogo(){
		do{
			personagem.executar();
			ambiente.evoluir();
		}while(ambiente.obterEvento() != EventoAmb.TERMINAR);
	}
	
	public static void main(String[]args){
		executarJogo();
	}
}

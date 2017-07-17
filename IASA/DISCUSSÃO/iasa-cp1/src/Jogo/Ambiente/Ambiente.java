package Jogo.Ambiente;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Ambiente {
	private Scanner sc = new Scanner(System.in);
	private Map<String,EventoAmb> tabelaEventos;
	private EventoAmb evento;
	
	public Ambiente(){
		evento = null;
		tabelaEventos = new HashMap<String,EventoAmb>();
		//preenchimento da tabela
		tabelaEventos.put("s",EventoAmb.SILENCIO);
		tabelaEventos.put("d",EventoAmb.DERROTA);
		tabelaEventos.put("f",EventoAmb.FUGA);
		tabelaEventos.put("i",EventoAmb.INIMIGO);
		tabelaEventos.put("r",EventoAmb.RUIDO);
		tabelaEventos.put("t",EventoAmb.TERMINAR);
		tabelaEventos.put("v",EventoAmb.VITORIA);
		
	}
	
	public void evoluir(){
		gerarEvento();
		mostrar();
	}
	
	public EventoAmb obterEvento(){
		return evento;
	}
	
	public void executarAccao(AccaoAmb accao){
		accao.executar();
	}
	
	private EventoAmb gerarEvento(){
		System.out.println("\n Evento?");
		//obtem input do utilizador
		String comando = sc.next();
		evento = tabelaEventos.get(comando);
		return evento;
	}
	
	private void mostrar(){
		if(evento != null){
			System.out.printf("Evento: %s\n",evento);
		}
	}
}

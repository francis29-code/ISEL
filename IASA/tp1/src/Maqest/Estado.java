package Maqest;

import java.util.HashMap;
import java.util.Map;

public class Estado<EV> {
	
	private String nome;
	private Map<EV,Estado<EV>> transicoes;
	
	public Estado(String nome){
		this.nome = nome;
		transicoes = new HashMap<EV,Estado<EV>>();
	}
	
	public String getNome(){
		return nome;
	}
	
	public Estado<EV> processar(EV evento){
		return transicoes.get(evento);
	}
	
	public Estado<EV> trans(EV estado, Estado<EV> evento){
		transicoes.put(estado, evento);
		return this;
	}
	
	public String toString(){
		return getNome();
	}
}

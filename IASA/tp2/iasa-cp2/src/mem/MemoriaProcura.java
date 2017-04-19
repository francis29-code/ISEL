package mem;

import java.util.HashMap;
import java.util.Queue;

import modProb.Estado;

public class MemoriaProcura {
	
	protected Queue<No> fronteira; 
	protected HashMap<Estado,No> explorados; 

	public MemoriaProcura(Queue<No> fronteira){
		this.fronteira = fronteira;
		this.explorados = new HashMap<Estado,No>();
	}
	
	public void limpar(){
		//limpa o array da queue
		explorados.clear();
		fronteira.clear();
	}
	
	public void inserir(No no){
		//adicionar à fronteira
		Estado estado = no.getEstado();
		No noMem = explorados.get(estado);
		if(noMem == null?true:no.getCusto() < noMem.getCusto()){
			fronteira.add(no);
			explorados.put(estado, no);
		}
	}
	
	public No remover(){
		//remove o primeiro elemento da queue
		return fronteira.poll();
	}
	
	public boolean fronteiraVazia(){
		return fronteira.isEmpty();
	}
}


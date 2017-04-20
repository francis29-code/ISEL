package mem;

import java.util.HashMap;
import java.util.Queue;

import modProb.Estado;

public class MemoriaProcura {
	
	protected Queue<No> fronteira; 
	protected HashMap<Estado,No> explorados; 
	private int complexidadeTemporal;

	public MemoriaProcura(Queue<No> fronteira){
		this.fronteira = fronteira;
		this.explorados = new HashMap<Estado,No>();
		this.complexidadeTemporal = 0;
	}
	
	public void limpar(){
		//limpa o array da queue
		explorados.clear();
		fronteira.clear();
	}
	
	public void inserir(No no){
		//adicionar à fronteira
		complexidadeTemporal++;
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
	
	public int getComplexidadeTemporal(){
		return fronteira.size();
	}
	
	public int getComplexidadeEspacial(){
		return complexidadeTemporal;
	}
}


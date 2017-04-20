package mecproc;

import mem.MemoriaProcura;
import mem.No;
import mem.Percurso;
import modProb.Estado;
import modProb.Operador;
import modProb.Problema;
import pee.Solucao;

public abstract class MecanismoProcura <P extends Problema>{
	private MemoriaProcura memoria_procura;
	protected P problema;
	private No no_inicial,no;
	
	public MecanismoProcura(){
		this.problema = null;
		this.no_inicial = null;
		this.no = null;
		this.memoria_procura = iniciarMemoria();
	}
	
	public Solucao resolver(P problema){
		//o integer é sempre o maximo possivel
		return resolver(problema,Integer.MAX_VALUE);
	}
	
	public Solucao resolver(P problema, int profMax){
		this.problema = problema;
		memoria_procura.limpar();
		no_inicial = new No(problema.getEstadoInicial());
		memoria_procura.inserir(no_inicial);
		
		while (!memoria_procura.fronteiraVazia()){
			no = memoria_procura.remover();
			if(problema.objectivo(no.getEstado())){
				return gerarSolucao(no);
			}else{
				if(no.getProfundidade() <= profMax){
					expandir(no);
					
				}
			}
		}
		return null;
	}
	
	private void expandir(No no){
		Estado estadoSuc = null;
		No noSuc = null;
		Estado estado = no.getEstado();
		Operador[] operadores = problema.getOperadores();
		
		for(Operador operador : operadores){
			estadoSuc = operador.aplicar(estado);
			if(estadoSuc != null){
				noSuc = new No(estadoSuc, operador, no);
				memoria_procura.inserir(noSuc);
			}
		}
	}
	
	private Solucao gerarSolucao(No noFinal){
		
		Percurso percurso = new Percurso();
		no = noFinal;
		No antecessor = null;
		
		while(no != null){
			percurso.juntarInicio(no);
			antecessor = no.getAntecessor();
			no = antecessor;
		}
		
		return percurso;
		
		
	}
	
	protected abstract MemoriaProcura iniciarMemoria();
	
	public int getComplexidadeTemporal(){
		return memoria_procura.getComplexidadeTemporal();
	}
	
	public int getComplexidadeEspacial(){
		return memoria_procura.getComplexidadeEspacial();
	}
}

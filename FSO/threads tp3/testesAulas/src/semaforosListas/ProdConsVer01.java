package semaforosListas;

import java.util.concurrent.Semaphore;

public class ProdConsVer01<T>{
	
	private Semaphore sPosLivres, sObjDisponiveis;
	private T dados[];
	private int idxG;
	private int idxP; 
	public ProdConsVer01(int dim){
		//criação do array generico
		this.dados = (T[]) new Object[dim];
		this.sPosLivres = new Semaphore(dim);
		this.sObjDisponiveis = new Semaphore(0);
		idxP= idxG =0;
	}
	
	public void put(T elem){
		try {
			sPosLivres.acquire();
			dados[idxP] = elem;
			idxP = (idxP+1)%dados.length;
			sObjDisponiveis.release();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}	
	}
	
	public T get(){
		T result = null;
		try {
			sObjDisponiveis.acquire();
			result = dados[idxG];
			idxG = (idxG+1)%dados.length;
			sPosLivres.release();
			
			
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		return result;
		
	}
}

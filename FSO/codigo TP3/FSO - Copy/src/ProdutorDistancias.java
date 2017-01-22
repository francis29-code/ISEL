import java.util.concurrent.Semaphore;

public class ProdutorDistancias {
	
	private CaixaCorreio cx;
	private Semaphore semaphore, distanciasLivres, distanciasOcupadas, acessoDistancias;
	int distancia;
	
	public ProdutorDistancias(CaixaCorreio cx, Semaphore ht){
		this.cx = cx;
		this.semaphore = ht;
		this.acessoDistancias = new Semaphore(1);
		this.distanciasLivres = new Semaphore(1);
		this.distanciasOcupadas = new Semaphore(0);
	}
	
	private void setDistancia(int distancia){
		try{
			distanciasLivres.acquire();
			acessoDistancias.acquire();
		}catch(Exception e){}
		cx.inserirElemento(this.distancia);
	}
}

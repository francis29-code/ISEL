
public class CaixaCorreio  {
	private Object objeto;

	public CaixaCorreio() {
		objeto = null;
	}

	public synchronized void inserirElemento(Object elem) {
		this.objeto = elem;
		
		this.notifyAll();
	}

	public synchronized Object  removerElemento() throws InterruptedException {
		while ( this.objeto==null ) {
			this.wait();
		}
		
		Object result = this.objeto;
		
		this.objeto = null;
		
		return result;
	}
}

/*
 * CaixaCorreio<Integer> mbInteger = new CaixaCorreio<Integer>();
 * CaixaCorreio<String> mbString = new CaixaCorreio<String>();
 * 
 * mbInteger.inserirElemento( new Integer( 1 ) );
 * 
 * ...
 * 
 * int xpto = mbInteger.removerElemento();
 * 
 * -----------------------------
 * 
 * CaixaCorreio mbInteger = new CaixaCorreio();
 * 
 * mbInteger.inserirElemento( new Integer( 1 ) );
 * 
 * ...
 * 
 * int xpto = (Integer)mbInteger.removerElemento();
 *
 */
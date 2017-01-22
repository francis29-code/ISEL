
public class CaixaCorreio /*<T>*/ {
	private /*T*/Object bufferCircular;

	public CaixaCorreio() {
		bufferCircular = null;
	}

	public synchronized void inserirElemento(/*T*/Object elem) {
		this.bufferCircular = elem;
		
		this.notifyAll();
	}

	public synchronized /*T*/Object  removerElemento() throws InterruptedException {
		while ( this.bufferCircular==null ) {
			this.wait();
		}
		
		/*T*/Object result = this.bufferCircular;
		
		this.bufferCircular = null;
		
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
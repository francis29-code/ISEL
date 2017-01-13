import java.util.concurrent.Semaphore;

public class CaixaCorreio {
	final int dimensaoBuffer = 2;
	String[] bufferCircular;
	int putBuffer, getBuffer;
	// o sem�foro elementosLivres indica se h� posi��es livres para inserir
	// Strings
	// o sem�foro acessoElemento garante exclus�o m�tua no acesso a um elemento
	// o sem�foro elementosOcupados indica se h� posi��es com Strings v�lidas
	Semaphore elementosLivres, acessoElemento, elementosOcupados;

	public CaixaCorreio() {
		bufferCircular = new String[dimensaoBuffer];
		putBuffer = 0;
		getBuffer = 0;
		elementosLivres = new Semaphore(dimensaoBuffer);
		elementosOcupados = new Semaphore(0);
		acessoElemento = new Semaphore(1);
	}

	public void inserirElemento(String s) {
		try {
			elementosLivres.acquire();
			acessoElemento.acquire();
			bufferCircular[putBuffer] = new String(s);
			putBuffer = ++putBuffer % dimensaoBuffer;
			acessoElemento.release();
		} catch (InterruptedException e) {
		}
		elementosOcupados.release();
	}

	public String removerElemento() {
		String s = new String();
		try {
			elementosOcupados.acquire();
			acessoElemento.acquire();
		} catch (InterruptedException e) {
		}
		s = bufferCircular[getBuffer];
		getBuffer = ++getBuffer % dimensaoBuffer;
		acessoElemento.release();
		elementosLivres.release();
		return s;
	}

}

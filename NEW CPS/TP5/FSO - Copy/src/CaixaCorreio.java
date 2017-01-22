import java.util.ArrayList;
import java.util.concurrent.Semaphore;

public class CaixaCorreio {
	final int dimensaoBuffer = 2;
	private ArrayList<Integer> bufferCircular;
	private int putBuffer, getBuffer;
	// o sem�foro elementosLivres indica se h� posi��es livres para inserir
	// Strings
	// o sem�foro acessoElemento garante exclus�o m�tua no acesso a um elemento
	// o sem�foro elementosOcupados indica se h� posi��es com Strings v�lidas
	private Semaphore elementosLivres, acessoElemento, elementosOcupados;

	public CaixaCorreio() {
		//arraylist ou estatico, opcional
		bufferCircular = new ArrayList<Integer>();
		putBuffer = 0;
		getBuffer = 0;
		elementosLivres = new Semaphore(dimensaoBuffer);
		elementosOcupados = new Semaphore(0);
		acessoElemento = new Semaphore(1);
	}

	public void inserirElemento(int distancia) {
		try {
			elementosLivres.acquire();
			acessoElemento.acquire();
			bufferCircular.add(putBuffer,distancia);
			putBuffer = ++putBuffer % dimensaoBuffer;
			acessoElemento.release();
		} catch (InterruptedException e) {
		}
		elementosOcupados.release();
	}

	public int removerElemento() {
		int s = new Integer(0);
		try {
			elementosOcupados.acquire();
			acessoElemento.acquire();
		} catch (InterruptedException e) {
		}
		s = bufferCircular.get(getBuffer);
		getBuffer = ++getBuffer % dimensaoBuffer;
		acessoElemento.release();
		elementosLivres.release();
		return s;
	}

}

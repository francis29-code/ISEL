import pee.PassoSolucao;
import pee.Solucao;
import puzzle.Puzzle;

public class ResolverPuzzle {

	
	public static void main(String [] args){
		
	}
	
	public OperadorPuzzle[] definirOperadores(){
		return new OperadorPuzzle[]{
				new OperadorPuzzle(Puzzle.Movimento.CIMA),
				new OperadorPuzzle(Puzzle.Movimento.ESQ),
				new OperadorPuzzle(Puzzle.Movimento.DIR),
				new OperadorPuzzle(Puzzle.Movimento.BAIXO)
		};
	}
	
	
	public void mostrarPuzzle(Solucao solucao){
		for(PassoSolucao passo : solucao){
			
		}
	}
}

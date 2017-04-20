import modProb.Estado;
import modProb.Operador;
import puzzle.Puzzle;
import puzzle.Puzzle.Movimento;

public class OperadorPuzzle implements Operador{

	private int custoJogada;
	private Movimento movimento;
	
	public OperadorPuzzle(Movimento movimento){
		//enumerado
		this.movimento = movimento;
		this.custoJogada = 1;
	}
	@Override
	public Estado aplicar(Estado estado){
		//transformações no espaço vazio do puzzle
		//movimentar o movimento do construtor
		Puzzle puzzle, newPuzzle;
		if(estado instanceof EstadoPuzzle){
			puzzle = ((EstadoPuzzle) estado).getPuzzle();
			newPuzzle = puzzle.movimentar(movimento);
			if(newPuzzle != null){
				return new EstadoPuzzle(newPuzzle);
			}
		}
		return null;
	}

	@Override
	public float custo(Estado estado, Estado estadoSuc) {
		return custoJogada;
	}
}

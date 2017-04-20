import modProb.Estado;
import modProb.Operador;
import modProb.Problema;
import puzzle.Puzzle;

public class ProblemaPuzzle extends Problema {
	
	private EstadoPuzzle puzzleFinal;

	public ProblemaPuzzle(Puzzle puzzleInicial, Puzzle puzzleFinal, OperadorPuzzle[] operadores) {
		super(new EstadoPuzzle(puzzleInicial), operadores);
		this.puzzleFinal = new EstadoPuzzle(puzzleFinal);
	}

	@Override
	public boolean objectivo(Estado estado) {
		//se o numPecasForaLugar for == 0, o puzzle está acabado
		Puzzle puzzle;
		if(estado instanceof EstadoPuzzle){
			puzzle = ((EstadoPuzzle) estado).getPuzzle();
			int nPecas = puzzle.numPecasForaLugar(puzzleFinal.getPuzzle());
			if(nPecas ==0){
				return true;
			}
		}
		return false;
	}
	
}

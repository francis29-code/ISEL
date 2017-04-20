import modProb.Estado;
import modProb.ProblemaHeur;
import puzzle.Puzzle;

public class ProblemaPuzzle extends ProblemaHeur {
	
	private EstadoPuzzle puzzleFinal;

	public ProblemaPuzzle(Puzzle puzzleInicial, Puzzle puzzleFinal, OperadorPuzzle[] operadores) {
		super(new EstadoPuzzle(puzzleInicial), operadores);
		this.puzzleFinal = new EstadoPuzzle(puzzleFinal);
	}
	
	@Override
	public boolean objectivo(Estado estado) {
		//se o numPecasForaLugar for == 0, o puzzle está acabado
		if(estado.equals(puzzleFinal)){
			return true;
		}
		return false;
	}

	@Override
	public double heuristica(Estado estado) {
		EstadoPuzzle estadoAtual = (EstadoPuzzle) estado;
		return estadoAtual.getPuzzle().distManhattan(puzzleFinal.getPuzzle());
	}
	
}

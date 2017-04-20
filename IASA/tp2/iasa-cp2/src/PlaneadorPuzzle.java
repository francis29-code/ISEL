import pee.PassoSolucao;
import pee.Solucao;
import prof.ProcuraLarg;
import puzzle.Puzzle;
import puzzle.Puzzle.Movimento;

public class PlaneadorPuzzle {
	
	static Puzzle puzzleInicialA = new Puzzle(new int[][]{
		{1,2,3},{8,4,5},{6,7,0}
	});
	static Puzzle puzzleInicialB = new Puzzle(new int[][]{
		{8,4,5},{6,1,2},{3,7,0}
	});
	static Puzzle puzzleFinal = new Puzzle(new int[][]{
		{1,2,3},{4,5,6},{7,8,0}
	});
	
	static ProcuraLarg plarg = new ProcuraLarg();
	static ProblemaPuzzle problemaA = new ProblemaPuzzle(puzzleInicialA,puzzleFinal,definirOperadores());
	static ProblemaPuzzle problemaB = new ProblemaPuzzle(puzzleInicialB,puzzleFinal,definirOperadores());
	
	public static void main(String [] args){
		final Solucao solLarg = plarg.resolver(problemaB);
		System.out.println("Procura por Largura");
		System.out.printf("Custo (Número Movimentos): %d",(int)solLarg.getCusto());
		System.out.println();
		mostrarPuzzle(solLarg);
	}
	
	public static OperadorPuzzle[] definirOperadores(){
		return new OperadorPuzzle[]{
				new OperadorPuzzle(Movimento.CIMA),
				new OperadorPuzzle(Movimento.ESQ),
				new OperadorPuzzle(Movimento.DIR),
				new OperadorPuzzle(Movimento.BAIXO)
		};
	}
	
	public static void mostrarPuzzle(Solucao solucao){
		System.out.println();
		for(PassoSolucao passo : solucao){
			//estado atual do puzzle num dos passos da solução
			System.out.println(passo.getEstado());
			System.out.println();
		}
	}
}

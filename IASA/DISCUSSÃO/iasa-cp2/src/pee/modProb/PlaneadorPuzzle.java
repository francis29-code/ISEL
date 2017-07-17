package pee.modProb;

import pee.PassoSolucao;
import pee.Solucao;
import pee.larg.ProcuraLarg;
import pee.mecproc.MecanismoProcura;
import pee.melhorprim.ProcuraAA;
import pee.melhorprim.ProcuraCustoUnif;
import pee.melhorprim.ProcuraSofrega;
import pee.prof.ProcuraProf;
import pee.prof.ProcuraProfIter;
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
	static ProcuraProfIter pfit = new ProcuraProfIter();
	static ProcuraProf pprof = new ProcuraProf();
	static ProcuraCustoUnif punif = new ProcuraCustoUnif();
	
	//procuras heuristicas
	static MecanismoProcura<ProblemaHeur> pAA = new ProcuraAA();
	static MecanismoProcura<ProblemaHeur> pSof= new ProcuraSofrega();
	
	//problemas iniciais
	static ProblemaPuzzle problemaA = new ProblemaPuzzle(puzzleInicialA,puzzleFinal,definirOperadores());
	static ProblemaPuzzle problemaB = new ProblemaPuzzle(puzzleInicialB,puzzleFinal,definirOperadores());
	
	public static void main(String [] args){
		final MecanismoProcura<Problema> currentMecanismo = plarg;
//		final MecanismoProcura<ProblemaHeur> currentMecanismo = pSof;
		final Solucao sol = currentMecanismo.resolver(problemaA);
		final int compEspacial = currentMecanismo.getComplexidadeEspacial();
		final int compTemporal = currentMecanismo.getComplexidadeTemporal();
//		mostrarPuzzle(sol);
		System.out.println();
		String [] procura = currentMecanismo.getClass().toString().split("\\.");
		System.out.printf("Procura por -> %s",procura[procura.length-1]);
		System.out.println();
		System.out.printf("Complexidade Temporal (expandidos): %d",compTemporal);
		System.out.println();
		System.out.printf("Complexidade Espacial (fronteira): %d",compEspacial);
		System.out.println();
		System.out.printf("Custo (Número Movimentos): %d",(int)sol.getCusto());
		System.out.println();
		
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
			System.out.print(passo.getEstado());
			System.out.println();
		}
	}
}

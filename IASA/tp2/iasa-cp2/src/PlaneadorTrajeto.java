

import melhorprim.OperadorLigacao;
import melhorprim.ProblemaPlanTraj;
import pee.PassoSolucao;
import pee.Solucao;
import prof.ProcuraCustoUnif;
import prof.ProcuraLarg;
import prof.ProcuraProf;
import prof.ProcuraProfIter;

public class PlaneadorTrajeto {
	
	static ProblemaPlanTraj problema = new ProblemaPlanTraj("Loc-0", "Loc-4", definirOperadores());
	static ProcuraProf pprof = new ProcuraProf();
	static ProcuraLarg plarg = new ProcuraLarg();
	static ProcuraProfIter pprofIt = new ProcuraProfIter();
	static ProcuraCustoUnif pcustoUnif = new ProcuraCustoUnif();
	
	public static void main(String []args){
		final Solucao solProf = pprof.resolver(problema);
		final Solucao solLarg = plarg.resolver(problema);
		final Solucao solPproIf = pprofIt.resolver(problema);
		final Solucao solCustoUnif = pcustoUnif.resolver(problema);
		System.out.println("Procura por Profundidade");
		System.out.printf("Dimensão : %d | ",solProf.getDimensao());
		System.out.printf("Custo: %1$.1f",solProf.getCusto());
		mostrarTrajeto(solProf);
		System.out.println();
		System.out.println("Procura por Largura");
		System.out.printf("Dimensão : %d | ",solLarg.getDimensao());
		System.out.printf("Custo: %1$.1f",solLarg.getCusto());
		mostrarTrajeto(solLarg);
		System.out.println();
		System.out.println("Procura por Profundidade-Iterativa");
		System.out.printf("Dimensão : %d | ",solPproIf.getDimensao());
		System.out.printf("Custo: %1$.1f",solPproIf.getCusto());
		mostrarTrajeto(solPproIf);
		System.out.println();
		System.out.println("Procura por Melhor Custo");
		System.out.printf("Dimensão : %d | ",solCustoUnif.getDimensao());
		System.out.printf("Custo: %1$.1f",solCustoUnif.getCusto());
		mostrarTrajeto(solCustoUnif);
		
	}
	
	private static OperadorLigacao[] definirOperadores(){
		return new OperadorLigacao[]{
				new OperadorLigacao("Loc-0","Loc-1",5),
				new OperadorLigacao("Loc-0","Loc-2",25),
				new OperadorLigacao("Loc-1","Loc-3",12),
				new OperadorLigacao("Loc-1","Loc-6",5),
				new OperadorLigacao("Loc-2","Loc-4",30),
				new OperadorLigacao("Loc-3","Loc-2",10),
				new OperadorLigacao("Loc-3","Loc-5",5),
				new OperadorLigacao("Loc-4","Loc-3",2),
				new OperadorLigacao("Loc-5","Loc-6",8),
				new OperadorLigacao("Loc-5","Loc-4",10),
				new OperadorLigacao("Loc-6","Loc-3",15),	
		};
	}
	
	private static void mostrarTrajeto(Solucao solucao){
		String trans = "";
		System.out.println();
		int aux=0;
		if(solucao != null){
			for(PassoSolucao passo : solucao){
				aux++;
				trans += passo.getEstado() + (solucao.getDimensao() > aux ? " -> "  : "");
			}
			System.out.printf("Transições: %s",trans);
			System.out.println();
		}
		
	}
}

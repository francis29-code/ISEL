import modProb.Estado;
import modProb.Operador;
import puzzle.Puzzle;

public class OperadorPuzzle implements Operador{

	int custoJogada;
	public OperadorPuzzle(Puzzle.Movimento movimento){
		//enumerado
		this.custoJogada = 1;
	}
	@Override
	public Estado aplicar(Estado estado){
		//cada jogada tem custo 1
		//transformações no espaço vazio do puzzle
		//movimentar o movimento do construtor
		return null;
	}

	@Override
	public float custo(Estado estado, Estado estadoSuc) {
		// TODO Auto-generated method stub
		return 0;
	}
}

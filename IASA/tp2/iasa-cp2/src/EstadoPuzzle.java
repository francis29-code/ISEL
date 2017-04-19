import modProb.Estado;
import puzzle.Puzzle;

public class EstadoPuzzle extends Estado{
	private Puzzle puzzle;
	public EstadoPuzzle(Puzzle puzzle){
		this.puzzle = puzzle;
	}
	
	@Override
	public int hashCode() {
		// TODO Auto-generated method stub
		return puzzle.hashCode();
	}
	
	
	@Override
	public String toString(){
		return puzzle.toString();
	}
	

}

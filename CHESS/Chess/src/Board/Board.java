package Board;

import java.awt.Color;
import java.awt.GridLayout;

import javax.swing.JPanel;

import Pieces.Piece;
import PlayPieces.Bishop;

public class Board extends JPanel{
	
	private static String [][] gameBoard = new String[][] {{"torre","cavalo","bispo","rainha","rei","bispo","cavalo","torre"},
		{"peao","peao","peao","peao","peao","peao","peao","peao"},
		{"vazio","vazio","vazio","vazio","vazio","vazio","vazio","vazio"},
		{"vazio","vazio","vazio","vazio","vazio","vazio","vazio","vazio"},
		{"vazio","vazio","vazio","vazio","vazio","vazio","vazio","vazio"},
		{"vazio","vazio","vazio","vazio","vazio","vazio","vazio","vazio"},
		{"peao","peao","peao","peao","peao","peao","peao","peao"},
		{"torre","cavalo","bispo","rei","rainha","bispo","cavalo","torre"}};
	
	private Piece[][] pieces;
		
	private static final long serialVersionUID = 1L;
	
	private static final int size = 8;
	
	private Moves moves;
	
	public Board(String pieceColours) {
		this.setLayout(new GridLayout(size, size));
		moves = new Moves(this);
		fillInitialBoard(pieceColours);
		this.setVisible(true);
		this.setOpaque(true);
		
	}
	
	private void fillInitialBoard(String pieceColours) {
		
		if(pieceColours.compareTo("pretas") ==0) {
			
		}
		
		for(int lines=0;lines<size;lines++){
			for(int columns=0;columns<size;columns++) {
				Bishop bishop = new Bishop(lines,columns,pieceColours);
				bishop.setBackground(Color.WHITE);
				bishop.addMouseListener(moves);
				this.add(bishop);
			}
		}
	}
	
	public void updateBoard() {

		System.out.println("dei update");
	}	
	
	public Piece[][] getBoard(){
		return pieces;
	}
	
}

package ChessGame;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Point;
import java.awt.Toolkit;

import javax.swing.JFrame;

import Board.Board;

public class ChessGame extends JFrame{

	private static final long serialVersionUID = 1L;
	private Board board;
	
	public ChessGame() {
		Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
		this.setSize(new Dimension(600,600));
		this.setLocation(new Point((int)dim.getWidth()/2-this.getWidth()/2, (int)dim.getHeight()/2-this.getHeight()/2));
		this.getContentPane().setBackground(Color.BLACK);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		board = new Board("branca");
		this.add(board);
		
	}

	
	public void showBoard() {
		this.setVisible(true);
	}
	
	public static void main(String [] args) {
		ChessGame chess = new ChessGame();
		
		chess.showBoard();
	}
}

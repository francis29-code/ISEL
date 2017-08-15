package Board;

import java.awt.Color;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import Pieces.Empty;

public class Moves extends MouseAdapter{
	
	private Board board;
	private int aux = 0;
	public Moves(Board board) {
		this.board = board;
	}

	@Override
	public void mousePressed(MouseEvent arg0) {
		// TODO Auto-generated method stub
		Empty empty = new Empty(1,1,"preto");
//		System.out.println(bishop.getIndex());
//		board.remove(bishop.getIndex() - aux);
//		board.remove(arg0.getComponent());
		arg0.getComponent().setBackground(Color.RED);
		aux++;
		board.repaint();
		
		
	}
	
//	@Override
//	public void mouseEntered(MouseEvent arg0) {
//		System.out.println(arg0.getComponent());
//		System.out.println("sdlçkmvklsdfmvklmdfklvfklm");
//	}

}

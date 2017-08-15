package Pieces;

import java.awt.Color;

import javax.swing.JLabel;
import javax.swing.border.LineBorder;

public abstract class Piece extends JLabel{
	
	private int x,y;
	private String color;
	
	public Piece(int x, int y,String color) {
		this.x = x;
		this.y = y;
		this.color = color;
		this.setOpaque(true);
		this.setBorder(new LineBorder(Color.BLACK));
	}
	
	public int getIndex() {
		return this.y + this.x*8;
	}
	
	public int[] getAixs() {
		return new int[] {this.x,this.y};
	}
	
	public abstract boolean canMove(int x, int y);

}

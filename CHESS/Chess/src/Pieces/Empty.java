package Pieces;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;

public class Empty extends Piece{
	
	private String color;
	public Empty(int x, int y, String color) {
		super(x, y,color);	
		this.color = color;
	}

	private static final long serialVersionUID = 1L;

	@Override
	public boolean canMove(int x, int y) {
		// TODO Auto-generated method stub
		return false;
	}
	
	@Override
	protected void paintComponent(Graphics g) {
		// TODO Auto-generated method stub
		super.paintComponent(g);
		this.setBackground(color == "preto" ? Color.BLACK : Color.WHITE);
		
	}

}

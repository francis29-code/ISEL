package PlayPieces;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import Pieces.Piece;

public class Bishop extends Piece{
	
	private BufferedImage image;
	private static final long serialVersionUID = 1L;

	public Bishop(int x, int y, String color) {
		super(x, y, color);
		try {
			if(color.compareTo("preta")==0) {
				image = ImageIO.read(new File("chessimages\\Chess_Pieces\\Black_Bishop.png"));
			}else {
				image = ImageIO.read(new File("chessimages\\Chess_Pieces\\White_Bishop.png"));
			}
		
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public boolean canMove(int x, int y) {
		// TODO Auto-generated method stub
		return false;
	}
	
	@Override
	protected void paintComponent(Graphics g) {
		// TODO Auto-generated method stub
		super.paintComponent(g);
		g.drawImage(image.getScaledInstance(this.getWidth(), this.getHeight(), Image.SCALE_SMOOTH), 0,0, null);
		
	}
	
	public void teste() {
		System.out.println("testestestets");
	}
	

}

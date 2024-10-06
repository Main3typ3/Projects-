package reversi;

import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JButton;

public class drawonbutton extends JButton {
	IModel model;
	IController controller;
	
	
	public void initialise( IModel model, IController controller) {
		this.model = model;
		this.controller = controller;
	}
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private boolean drawCircle = false;
	private int color;
	
	

	@Override
	protected void paintComponent(Graphics g) {
		// TODO Auto-generated method stub
		
		super.paintComponent(g);
				
		
	if (drawCircle) {
		if(this.color == 1) {
			g.setColor(Color.WHITE);
			g.fillOval(getHorizontalAlignment(), getVerticalAlignment(), getWidth() - 2, getHeight()-2);
		}
		
		if(this.color == 2) {
			g.setColor(Color.BLACK);
			g.fillOval(getHorizontalAlignment(), getVerticalAlignment(), getWidth() - 2, getHeight()-2);
		}
		
		if(this.color == 0) {
			g.setColor(null);
			//g.setColor(new Color(3,125,80));
			//g.fillOval(getHorizontalAlignment(), getVerticalAlignment(), getWidth() - 2, getHeight()-2);
		}
        
     }
	 
	
	}
	
	 public void setDrawCircle(boolean drawCircle,int color) {
	     this.drawCircle = drawCircle;
	     this.color = color;
	     repaint();
	     
	     
	     
	 }
	 
	 
	
 }




	


package reversi;

import java.awt.BorderLayout;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.GridLayout;

import javax.swing.BorderFactory;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class GUIView  implements IView {
	
	IModel model;
	IController controller;
	
	JLabel message1 = new JLabel();

	JTextArea board1 = new JTextArea();
	JTextArea board2 = new JTextArea();
	JFrame frame1 = new JFrame();
	JLabel feedbacktop1 = new JLabel();
	JLabel feedbacktop2 = new JLabel();
	JLabel title = new JLabel();

	JTextArea f2Board = new JTextArea();
	JFrame frame2 = new JFrame();
	
	drawonbutton[][] orthelloBoardSquaresF2 = new drawonbutton[8][8];
    drawonbutton[][] orthelloBoardSquares = new drawonbutton[8][8];
    
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// IView views = new IView(); 
	}
	
	@Override
	public void initialise( IModel model, IController controller ) {
		
		this.model = model;
		this.controller = controller;		
		// Create a dummy user interface - you need to do a proper one in your implementation
		// You will need 2 frames but I put only one into the demo
		frame1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame1.setTitle("Player 1");
		
		
		frame1.setLocationRelativeTo(null); // centre on screen
		frame1.setSize(700, 700);
		
		board1.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5) );
		JPanel p1Panel = new JPanel();
		
		p1Panel.setBorder( BorderFactory.createLineBorder(Color.LIGHT_GRAY,3) );
		p1Panel.setLayout( new BorderLayout() );
		frame1.add(p1Panel,BorderLayout.NORTH);
		
		JPanel p2Panel = new JPanel();
		p2Panel.setBorder( BorderFactory.createLineBorder(Color.LIGHT_GRAY,3) );
		p2Panel.setLayout(new GridLayout(model.getBoardHeight(),model.getBoardWidth()));
	    int i;
	    int j;
	    int l;
	    int p;
	    
	    
	    // frame 2 player 2 stuff
	    
	    frame2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame2.setTitle("Player 2");
		frame2.setLocationRelativeTo(null); // centre on screen
		frame2.setSize(700, 700);
		
		f2Board.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5) );
		JPanel F2P1Panel = new JPanel();
		F2P1Panel.setBorder( BorderFactory.createLineBorder(Color.LIGHT_GRAY,3) );
		F2P1Panel.setLayout( new BorderLayout() );
		frame2.add(F2P1Panel,BorderLayout.NORTH);
		
		JPanel F2P2Panel = new JPanel();
		F2P2Panel.setBorder( BorderFactory.createLineBorder(Color.LIGHT_GRAY,3) );
		F2P2Panel.setLayout(new GridLayout(model.getBoardHeight(),model.getBoardWidth()));
	   
	    
	   
	    
	    l = model.getBoardHeight() -1 ;
	    p = model.getBoardWidth() -1 ;
	    
	    
	    for(i = 0; i < model.getBoardHeight() ; i ++ ) {
	    	
	    	
	    	for(j = 0; j < model.getBoardWidth() ; j++ ) {
	    		
	    	
	    		 
	    	orthelloBoardSquares[i][j] = new drawonbutton();
	    	orthelloBoardSquares[i][j].initialise(model,controller);
	    	
	    	
	    	orthelloBoardSquares[i][j].setBackground(new Color(3,125,80));
	    	orthelloBoardSquares[i][j].setPreferredSize(new Dimension(40, 40));
	    	p2Panel.add(orthelloBoardSquares[i][j]);
	    	
	    	orthelloBoardSquaresF2[l][p] = new drawonbutton();
	    	orthelloBoardSquaresF2[l][p].initialise(model,controller);
	    	orthelloBoardSquaresF2[l][p].setBackground(new Color(3,125,80));
	    	orthelloBoardSquaresF2[l][p].setPreferredSize(new Dimension(40, 40));
	    	F2P2Panel.add(orthelloBoardSquaresF2[l][p]);
	    	
	    	
	    	final int player0 = 1;
	    	final int rowp1 = i;
	    	final int  columnp1 = j;
	    	
	    	orthelloBoardSquares[i][j].addMouseListener(new MouseAdapter() { 
	    	    public void mousePressed(MouseEvent me) {
	            	//model.setBoardContents(rowp1,columnp1,player0);
	                
	                controller.squareSelected(player0, rowp1, columnp1);
	               
	                //orthelloBoardSquaresF2[rowp1][columnp1].setDrawCircle(true);
	                //orthelloBoardSquares[rowp1][columnp1].setDrawCircle(true);
	                //System.out.println("row = " + rowp1 + "column = " + columnp1);
	                //refreshView();
	                
	          
	            } 
	          }); 
	    	
	    	final int player1 = 2;
	    	final int rowp2 = l;
	    	final int  columnp2 = p;
	    	
	    	orthelloBoardSquaresF2[l][p].addMouseListener(new MouseAdapter() { 
	    	    public void mousePressed(MouseEvent me) {
                
                	//model.setBoardContents(rowp2,columnp2,player1);
                	controller.squareSelected(player1, rowp2, columnp2);
                	
                	//orthelloBoardSquaresF2[rowp2][columnp2].setDrawCircle(true);
                	//orthelloBoardSquares[rowp2][columnp2].setDrawCircle(true);
                	//System.out.println("row = " + rowp2 + "column = " + columnp2);
                	//refreshView();
                	
                }
            });
   
	    	p--;
	    	}
	    	l--;
	    	p = model.getBoardWidth() - 1;
	    }
	    
		//p2Panel.setSize(700, 700);
		frame1.add(p2Panel,BorderLayout.CENTER);
		
		JPanel p3Panel = new JPanel();
		p3Panel.setBorder( BorderFactory.createLineBorder(Color.LIGHT_GRAY,3) );
		p3Panel.setLayout( new BorderLayout() );
		frame1.add(p3Panel,BorderLayout.SOUTH);
		message1.setFont( new Font( "Arial", Font.BOLD, 20 ));
		board1.setFont( new Font( "Consolas", Font.BOLD, 20 ));
		// Now we add the 'stuff' for each player to the panel for that player...
		message1.setText("White Player Player 1");
		
		feedbacktop1.setText("it is now your turn");
		p1Panel.add(feedbacktop1,BorderLayout.SOUTH);
		p1Panel.add(message1,BorderLayout.NORTH);
		// AI button
		JButton butAI1 = new JButton(" Greedy AI 1");
		butAI1.addActionListener( new ActionListener() 
					{ public void actionPerformed(ActionEvent e) { controller.doAutomatedMove(1); } } );
		p3Panel.add(butAI1,BorderLayout.NORTH);
		
		//restart button
		JButton Refresh2 = new JButton(" Restart");
		Refresh2.addActionListener( new ActionListener() 
					{ public void actionPerformed(ActionEvent e) { controller.startup(); } } );
		p3Panel.add(Refresh2,BorderLayout.SOUTH);
		frame1.pack();
		frame1.setVisible(true);
		frame2.add(F2P2Panel,BorderLayout.CENTER);
		
		JPanel F2P3Panel = new JPanel();
		F2P3Panel.setBorder( BorderFactory.createLineBorder(Color.LIGHT_GRAY,3) );
		F2P3Panel.setLayout( new BorderLayout() );
		frame2.add(F2P3Panel,BorderLayout.SOUTH);
		title.setFont( new Font( "Arial", Font.BOLD, 20 ));
		f2Board.setFont( new Font( "Consolas", Font.BOLD, 20 ));
		// Now we add the 'stuff' for each player to the panel for that player...
		title.setText("Black Player Player 2");
		F2P1Panel.add(feedbacktop2,BorderLayout.SOUTH);
		F2P1Panel.add(title,BorderLayout.NORTH);
		
		// AI button
		JButton F2AI = new JButton(" Greedy AI  2");
		F2AI.addActionListener( new ActionListener() 
					{ public void actionPerformed(ActionEvent e) { controller.doAutomatedMove(2); } } );
		F2P3Panel.add(F2AI,BorderLayout.NORTH);
		
		//restart button
		JButton RefreshF2 = new JButton(" Restart");
		RefreshF2.addActionListener( new ActionListener() 
					{ public void actionPerformed(ActionEvent e) { controller.startup(); } } );
		F2P3Panel.add(RefreshF2,BorderLayout.SOUTH);
		frame2.pack();
		frame2.setVisible(true);
	
	}
	
	
	

	@Override
	public void refreshView() {
		int i ,j , k, l;
		int w =1;
		int b = 2;
		int g = 0;
		
		//System.out.println("board is ");
		for(i=0; i < model.getBoardHeight(); i++) {
			for (j=0; j < model.getBoardWidth(); j++) {
				//System.out.print(model.getBoardContents(i, j));
				
				if(model.getBoardContents(i, j) == 1) {
					orthelloBoardSquares[i][j].setDrawCircle(true,w);
				}
				
				if(model.getBoardContents(i, j) == 2) {
					orthelloBoardSquares[i][j].setDrawCircle(true,b);
				}
				if(model.getBoardContents(i, j) == 0) {
					orthelloBoardSquares[i][j].setDrawCircle(true,g);
				}
				
			}	
			//System.out.println("");
		}
		
		for(k= model.getBoardHeight() -1; k > -1 ; k--) {
			for (l= model.getBoardWidth() -1 ; l > -1 ; l--) {
				//System.out.print(model.getBoardContents(k, l));
				
				if(model.getBoardContents(k, l) == 1) {
					orthelloBoardSquaresF2[k][l].setDrawCircle(true,w);
				}
				
				if(model.getBoardContents(k, l) == 2) {
					orthelloBoardSquaresF2[k][l].setDrawCircle(true,b);
				}
				
				if(model.getBoardContents(k, l) == 0) {
					orthelloBoardSquaresF2[k][l].setDrawCircle(true,g);
				}
				
				
			}	
			//System.out.println("");
		}
		
		
		
		
	
	}
	
	@Override
	public void feedbackToUser( int player, String message ) {
		
		if ( player == 1 ) {
			feedbacktop1.setText(message);
		}
		else if ( player == 2 ) {
			feedbacktop2.setText(message);
		}
		
	}	

}



		

	
	
	


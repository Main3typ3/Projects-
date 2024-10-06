package reversi;

public class ReversiController implements IController {
	
	
	IModel model;
	IView view;
	int count1 = 0;
	int count2 = 0;
	int count3 = 0;
	int count4 = 0;
	int count5 = 0;
	int count6 = 0;
	int count7 = 0;
	int count8 = 0;
	int play1finish;
	int play2finish;
	

	
	
	@Override
	public void initialise( IModel model, IView view ) {
		this.model = model;
		this.view = view;
		
	}
	
	
	
	
	@Override
	public void startup() {
		int width = model.getBoardWidth();
		int height = model.getBoardHeight();
		
		for ( int x = 0 ; x < width ; x++ )
			for ( int y = 0 ; y < height ; y++ )
				model.setBoardContents(x, y, 0);
		
		model.setBoardContents(4, 3, 2);
		model.setBoardContents(3, 3, 1);
		model.setBoardContents(3, 4, 2);
		model.setBoardContents(4, 4, 1);
		model.setPlayer(1);
		view.feedbackToUser(1, "White player – choose where to put your piece");
		view.feedbackToUser(2, "Black player – not your turn");
		model.setFinished(false);
		view.refreshView();		
	}
	
	
	
	
	
	@Override
	public void update() {
		boolean full = true;
		boolean finished = false;
		int p1 ;
		int p2 ;
		
		
		for ( int x = 0 ; x < model.getBoardWidth() ; x++ )
			for ( int y = 0 ; y < model.getBoardHeight() ; y++ )
				if ( model.getBoardContents(x, y) == 0 )
					full = false; // There is an empty square
		
		play1finish = 0;
		play2finish = 0;
		int valid1 = checkifvalidspaces(1 , 2);
		int valid2 = checkifvalidspaces(2 , 1);
		if (valid1 == 0) {
			play1finish = 1;
			model.setPlayer(2);
		}
		
		if (valid2 == 0) {
			play2finish = 1;
			model.setPlayer(1);
		}
		
		if(  ( (play1finish == 1)&& (play2finish == 1 )  ) || (full ==true)  ) {
			p1= 0;
			p2 = 0;
			finished = true;
			for ( int x = 0 ; x < model.getBoardWidth() ; x++ ) {
				for ( int y = 0 ; y < model.getBoardHeight() ; y++ ) {
					if(model.getBoardContents(x, y) == 1) {
						p1++;
					}
					if(model.getBoardContents(x, y) == 2) {
						p2++;
					}
					
				}
			}
			if (p1 > p2) {
				view.feedbackToUser(1,"White won. White " + p1 + " to Black " + p2+ " . Reset game to replay ");
				view.feedbackToUser(2,"White won. White " + p1 + " to Black " + p2+ " . Reset game to replay ");
				
			}
			if (p2> p1) {
				view.feedbackToUser(1,"Black won. Black " + p2 + " to White " + p1+ " . Reset game to replay ");
				view.feedbackToUser(2,"Black won. Black " + p2 + " to White " + p1+ " . Reset game to replay ");
				
			}
			if (p2 == p1) { 
				view.feedbackToUser(1,"Draw. Both players ended with " +p1+ " pieces. Reset game to replay. ");
				view.feedbackToUser(2,"Draw. Both players ended with " +p1+ " pieces. Reset game to replay. ");
				
			}
			
		}
		
		model.setFinished(finished);
		
		if(model.hasFinished() == false) {
			
		int player2 = model.getPlayer();
		
		
		
		if(player2 == 1 ) {
		
			view.feedbackToUser(1, "White player – choose where to put your piece");
			view.feedbackToUser(2, "Black player – not your turn");
		
		
		}
		
		if(player2 == 2 ) {
		
			view.feedbackToUser(1, "White player – not your turn");
			view.feedbackToUser(2, "Black player – choose where to put your piece");
		
		
		
		}
		
	 }
		
	}
	
	
	public int checkifvalidspaces(int player ,int oppositeplayer) {
		int i, j,valid_spaces = 0,v9 = 0;
		
		for(i=0; i < model.getBoardHeight(); i++) {
			for (j=0; j < model.getBoardWidth(); j++) {
				if(model.getBoardContents(i, j) != 0) {
					continue;
				}
				else {
					v9 = valididty(player, i,j,oppositeplayer);
					if(v9 == 1) {
						valid_spaces++;
					}
				}
				
			}	
			
		}
		
		return valid_spaces;
		
	}
	
	
	
	
	@Override
	public void doAutomatedMove( int player ) {
		int i, j,v9,oppositeplayer = 10,total_count,holder_count = 0,g =0,h = 0,valid_spaces = 0;
		
		if(player != model.getPlayer()) {
			return;
			
		}
		
		if(player == 1) {
			oppositeplayer = 2;
		}
		if(player == 2) {
			oppositeplayer = 1;
		}
		
		for(i=0; i < model.getBoardHeight(); i++) {
			for (j=0; j < model.getBoardWidth(); j++) {
				
				
				if(model.getBoardContents(i, j) != 0) {
					continue;
					
				}
				else {
					v9 = valididty(player, i,j,oppositeplayer);
					if(v9 == 1) {
						valid_spaces++;
						//System.out.println(" amount of valid spaces avalible = "+valid_spaces+ " in space x = "+i + " in space y = "  + j);
						total_count = count1+count2+count3+count4+count5+count6+count7+count8;
						if (total_count > holder_count) {
							holder_count = total_count;
							g = i;
							h = j;
						}
					}
				}
				
			}	
			
		}
		
		squareSelected(player,g,h);
	}
	
	
	
	
	
	
	
	public int valididty (int player,int x ,int  y,int oppositeplayer) {
		int v1 = 0 ,v2 = 0,v3 = 0,v4 = 0,v5 = 0,v6 = 0,v7 = 0,v8 = 0,v9 =0,lastvalue =10;
		count1 =0;
		count2 =0;
		count3 =0;
		count4 =0;
		count5 =0;
		count6 =0;
		count7 =0;
		count8 =0;
		
		int i ;
		
		for(i = (x + 1 ); i < model.getBoardHeight() ; i++) {
		
			
			
			if(model.getBoardContents(i, y) != oppositeplayer) {
				lastvalue = model.getBoardContents(i, y) ;
				if ((lastvalue == player) && (count1 != 0)) {
					v1 = 1;
				}
				else {
					count1 = 0;
				}
				break;
			}

			if(model.getBoardContents(i, y) == oppositeplayer) {
				count1++;
				
			}	
		}
		
		for(i = (x-1) ; i > -1; i--) {
			
			
			if(model.getBoardContents(i, y) != oppositeplayer) {
				lastvalue = model.getBoardContents(i, y) ;
				if (lastvalue == player && (count2 != 0)) {
					v2 = 1;
				}
				else {
					count2 = 0;
				}
				break;
			}
			
			if(model.getBoardContents(i, y) == oppositeplayer) {
				count2++;
			}
		}


		for(i = (y + 1 ); i < model.getBoardHeight() ; i++) {
			
			if(model.getBoardContents(x, i) != oppositeplayer) {
				lastvalue = model.getBoardContents(x, i) ;
				if (lastvalue == player  && (count3 != 0)) {
					v3 = 1;
				}
				else {
					count3 = 0;
				}
				break;
			}
			
			if(model.getBoardContents(x, i) == oppositeplayer) {
				count3++;
			}	
		}
		
		for(i = (y-1) ; i > -1; i--) {
			
			
			if(model.getBoardContents(x, i) != oppositeplayer) {
				lastvalue = model.getBoardContents(x, i) ;
				if (lastvalue == player && (count4 != 0)) {
					v4 = 1;
				}
				else {
					count4 = 0;
				}
				break;
			}
			
			if(model.getBoardContents(x, i) == oppositeplayer) {
				count4++;
			}
			
		}

		//diagonal bottom right
		
		
		int z = y + 1;
		for(i = (x + 1 ); i < model.getBoardHeight() ; i++) {
			
			if(z > 7) {
				break;
			}
			
		 	if(model.getBoardContents(i, z) != oppositeplayer) {
				lastvalue = model.getBoardContents(i, z) ;
				if (lastvalue == player && (count5  != 0)) {
					v5 = 1;
				}
				else {
					count5 = 0;
				}
				break;
			}
		 	
		 	if(model.getBoardContents(i, z) == oppositeplayer) {
				count5++;
			}
			z++;				
		}
			
		

		
		z = y - 1;
		for(i = (x + 1 ); i < model.getBoardHeight() ; i++) {
			
			if(z < 0) {
				break;
			}
			
			
			
		 	if(model.getBoardContents(i, z) != oppositeplayer) {
				lastvalue = model.getBoardContents(i, z) ;
				if (lastvalue == player  && (count6  != 0)) {
					v6 = 1;
				}
				else {
					count6 = 0;
				}
				break;
			}
		 	
		 	if(model.getBoardContents(i, z) == oppositeplayer) {
				count6++;
			}
			z--;				
		}
			
	
		
		//diagnoal top right
		
		z = y + 1;
		for(i = (x - 1 ); i > -1 ; i--) {
			
			if(z > 7) {
				break;
			}
		 	if(model.getBoardContents(i, z) != oppositeplayer) {
				lastvalue = model.getBoardContents(i, z) ;
				if (lastvalue == player && (count7  != 0)) {
					v7 = 1;
				}
				else {
					count7 = 0;
				}
				break;
			}
		 	if(model.getBoardContents(i, z) == oppositeplayer) {
				count7++;
			}
			z++;				
		}
			
		
		//diagnoal top left
		
		z = y - 1;
		
		for(i = (x - 1 ); i > -1 ; i--) {
			
			if(z < 0) {
				break;
			}
		 	if(model.getBoardContents(i, z) != oppositeplayer) {
				lastvalue = model.getBoardContents(i, z) ;
				if (lastvalue == player && (count8  != 0)) {
					v8 = 1;
				}
				else {
					count8 = 0;
				}
				break;
			}
		 	if(model.getBoardContents(i, z) == oppositeplayer) {
				count8++;
			}
			z--;
		}
		
		
		if((v1 == 1) || (v2==  1) || (v3 ==1 ) || (v4 ==1) || (v5 ==1 ) || (v6 ==1) || (v7 ==1 ) ||( v8 ==1)) {
			v9 = 1;
		}
		return v9;
		
	}
	
	@Override
	public void squareSelected( int player, int x, int y ) {
		
		int oppositeplayer = 10;
		int i,j,l ,valid = 0;
		
		if(model.hasFinished() == true) {
			return;
		}
		
		if(player == 1) {
			oppositeplayer = 2;
		}
		
		if(player == 2) {
			oppositeplayer = 1;
		}
		
		if(player != model.getPlayer()) {
			view.feedbackToUser(player ,"It is not your turn!");
			return;
		}
		
		if(model.getBoardContents(x, y) != 0) {
			view.feedbackToUser(player, "You cant place that there, Try again" );
			return;
		}
		
		
		
int v9 = valididty( player, x , y,oppositeplayer);
		
		if(v9 == 1) {
			
			//&& (v1 == 1)
			if((count1 != 0)  ) {
				
				j = x+1;
				for(i = 0; i < count1 ; i++) {
					model.setBoardContents(j,y , player);
					j++;
				}
			}
			
			//&& (v2 == 1)
			if(count2 != 0 ) {
				j = x-1;
				for(i = 0; i < count2 ; i++) {
					model.setBoardContents(j,y , player);
					j--;
				}
			}
			
			//&& (v3 == 1)
			if((count3 != 0)) {
				j = y +1;
				for(i = 0; i < count3 ; i++) {
					model.setBoardContents(x,j , player);
					j++;
				}
			}
			
			// && (v4 == 1)
			if((count4 != 0) ) {
				j = y-1;
				for(i = 0; i < count4 ; i++) {
					model.setBoardContents(x,j , player);
					j--;
				}
			}
			
			//&& (v5 == 1)
			if((count5 != 0) ) {
				l = x+1;
				j = y+1;
				for(i = 0; i < count5 ; i++) {
					model.setBoardContents(l,j, player);
					l++;
					j++;	
				}	
			}
			
			//&& (v6 == 1)
			if((count6 != 0)) {
				l = x+1;
				j = y-1;
				for(i = 0; i < count6 ; i++) {
					model.setBoardContents(l,j, player);
					l++;
					j--;	
				}
			}
			
			//&& (v7 == 1)
			if((count7 != 0) ) {
				l = x-1;
				j = y+1;
				for(i = 0; i < count7 ; i++) {
					model.setBoardContents(l,j, player);
					l--;
					j++;
				}
			}
			
			//&& (v8 == 1)
			if((count8 != 0) ) {
				l = x-1;
				j = y-1;
				for(i = 0; i < count8 ; i++) {
					model.setBoardContents(l,j, player);
					l--;
					j--;
				}
			}
			
			model.setBoardContents(x, y, player);		
			view.refreshView();
			
			
		//	valid = checkifvalidspaces(oppositeplayer , player);
		//	System.out.println("valid is = "+ valid);
		//	if (valid == 0) {
			//	if (oppositeplayer == 1) {
			//		model.setPlayer(player);
			//		play1finish = 1;
			//	
			//	}
			//	
			//	if (oppositeplayer == 2) {
			//		model.setPlayer(player);
			//		play2finish = 1;
			//	}
			
			//}
			
			//System.out.println("player is = " + player);
			//System.out.println("model player is = " + model.getPlayer());
			
			//System.out.println("model player is after changing it = " + model.getPlayer());
			
			//model.setPlayer(player);
			
			
			
				if(player == 1) {
			    	//view.feedbackToUser(player, "White player – not your turn");
					model.setPlayer(oppositeplayer);
					//view.feedbackToUser(oppositeplayer, "Black player – choose where to put your piece");
				}
				if(player == 2) {
					//view.feedbackToUser(player, "Black player – not your turn");
					model.setPlayer(oppositeplayer);
					//view.feedbackToUser(oppositeplayer, "White player – choose where to put your piece");
				}
				
			update();
			}
		
		//update();
		return;
		
		
		
		
		
	}

}

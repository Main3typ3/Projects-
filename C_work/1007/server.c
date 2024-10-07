/*
 *  NetworkServer.c
 *  COMP1007 Large Coursework 02 Skeleton
 *
 */

/* You will need to include these header files to be able to implement the TCP/IP functions */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <sys/socket.h>
#include "graph.h"
#include "dijkstra.h"

/* You will also need to add #include for the graph library header files */

void ServerConnection(int sd);
void ReadLineFromNetwork(int sd, char *buf, int size);
void printplusok(int sd);
void printminuserror(int sd);

void printplusok1(int sd);

void printendpulse(int sd);
void netaddroutine(int sd, int holder1);
void netDeleteroutine(int sd, int holder1);
void netlistRoutine(int sd);
void routeAddroutine(int sd, int holder1,int holder2,int holder3);
void RouteDeleteRoutine(int sd, int holder1, int holder2);
void RouteShowroutine(int sd, int holder1);
void RouteHopRoutine(int sd, int holder1,int holder2);
void RouteTableRoutine(int sd, int holder1);


Graph *graphtohandle;
Edge *edgey;
Edge **edgey2;
Edge *edgey3;
Vertex *nullhandler;
Vertex *nullhandler1;
Path *array;
Path *array2;




int main(int argc, const char * argv[])
{
	
	int serverSocket = -1;
	int connectionSocket;
	struct sockaddr_in server;
	struct sockaddr_in client;
	unsigned int alen;
	int newport;
	
	newport = strtol(argv[1],NULL,10);
	
	printf("COMP1007 Route Server Implementation\n");
	printf("====================================\n\n");
	
	
	
	/* Set up socket */
	serverSocket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
	if(serverSocket == -1)
	{
		fprintf(stderr, "Failed to create socket\n");
		exit(1);
	}
	
	/* Setup the socket port */
	memset(&server, 0, sizeof(struct sockaddr_in));
	server.sin_family = AF_INET;
	server.sin_port = htons(newport);
	server.sin_addr.s_addr = INADDR_ANY;
	
	if(bind(serverSocket, (struct sockaddr *)&server, sizeof(struct sockaddr_in)) < 0)
	{
		fprintf(stderr, "Failed to bind()\n");
		exit(2);
	}
	
	
	if(listen(serverSocket, 15) < 0)
	{
		fprintf(stderr, "Failed to listen()\n");
		exit(3);
	}
	printf("we are listening for your connnection\n");
	graphtohandle = init_graph();
	while(1)
	{
		alen = sizeof(client);
		connectionSocket = accept(serverSocket, (struct sockaddr *)&client, &alen);
		printf("Connection from %x on port %d\n", ntohl(client.sin_addr.s_addr), ntohs(client.sin_port));
		

		/* Communicate over the socket / access */
		
		ServerConnection(connectionSocket);
		/* Close */

		close(connectionSocket);
		
	}
	return 0;
}

	
	/* Insert your code here to create, and the TCP/IP socket for the Network Server
	 *
	 * Then once a connection has been accepted implement protocol described in the coursework description.
	 */
	
	
void ServerConnection(int sd)
{
   	int state = 0;
	char line[256];
	char output[256];
	char stringtouse[256];
	int holder1, holder2, holder3;

	char *netadd = "NET-ADD";
 	char *netdelete = "NET-DELETE";
 	char *netlist = "NET-LIST";
 	char *routeadd = "ROUTE-ADD";
 	char *routedelete = "ROUTE-DELETE";
 	char *routeshow = "ROUTE-SHOW";
 	char *routehop = "ROUTE-HOP";
 	char *routetable = "ROUTE-TABLE";
 	char *QUIT = "QUIT";
    char *comp1007 = "+OK 2023 COMP1007 Route Server\r\n";
    
	
    
	write(sd,comp1007, strlen(comp1007));
    
	while(state == 0 ){
    	ReadLineFromNetwork(sd,line,256);
		printf("Client sent [%s]\n", line);
        holder1 = 0;
		holder2 = 0;
		holder3 = 0;
		sscanf(line, "%s %d %d %d",stringtouse,&holder1,&holder2,&holder3);
		printf("first part is %s, Secondpart is %d, third part is %d, this is the last part %d\n",stringtouse,holder1,holder2,holder3);

		if(strcmp(stringtouse,netadd) == 0){
			netaddroutine(sd, holder1);
		}
		else if(strcmp(stringtouse,netdelete) == 0){
			netDeleteroutine(sd, holder1);
			
		}
		else if(strcmp(stringtouse,netlist) == 0){
			netlistRoutine(sd);
		}

		else if(strcmp(stringtouse,routeadd) == 0){
			
			routeAddroutine(sd ,holder1,holder2,holder3);
		}

		else if(strcmp(stringtouse,routedelete) == 0){
			
			RouteDeleteRoutine(sd, holder1,holder2);
			
		}
		else if(strcmp(stringtouse,routeshow) == 0){
			RouteShowroutine(sd,holder1);
		}
		else if(strcmp(stringtouse,routehop) == 0){
			RouteHopRoutine(sd, holder1, holder2);
		}
		else if(strcmp(stringtouse,routetable) == 0){
			RouteTableRoutine(sd,holder1);
		}


		else if (strcmp(stringtouse,QUIT)== 0){
			printplusok(sd);
			state = 1;
		
		}

		else{
			printminuserror(sd);
		}
	}

}


void netaddroutine(int sd, int holder1){
	int newholder;
	char *added = "Added ";
	char num[256];
	newholder = holder1;
	sprintf(num,"%d",newholder);

	nullhandler = find_vertex(graphtohandle, newholder);
    if (nullhandler == NULL){
		add_vertex(graphtohandle, newholder);
		printplusok1(sd);
		write(sd,added,strlen(added));
		write(sd,num ,strlen(num));
		printendpulse(sd);
	}
	else{
		printminuserror(sd);
	}
	


}
void netDeleteroutine(int sd, int holder1){
	int newholder;
	char num[256];
	char *deleted = "Deleted ";
	newholder = holder1;
	sprintf(num,"%d",newholder);
	nullhandler = find_vertex(graphtohandle, newholder);
	if(nullhandler != NULL ){
		remove_vertex(graphtohandle,newholder);
		printplusok1(sd);
		write(sd,deleted,strlen(deleted));
		write(sd,num,strlen(num));
		printendpulse(sd);

	}
	else{
		printminuserror(sd);
	}
    
}

void netlistRoutine(int sd){
	int i;
	int count = 0;
	char num[256];
	int *pointertoverticies;
	char num2[256];
	pointertoverticies = get_vertices(graphtohandle,&count);

	sprintf(num,"%d",count);
	printplusok1(sd);
	write(sd,num,strlen(num));
	printendpulse(sd);

	for(i=0; i<count ; i++){
	sprintf(num2,"%d",*(pointertoverticies + i));
	write(sd,num2,strlen(num2));
	printendpulse(sd);
	}
   

}

void routeAddroutine(int sd,int holder1,int holder2,int holder3){
	int newholder1,newholder2;
	double newholder3;
	char *routeadded1 = "Route Added ";
	newholder1 = holder1;
	newholder2 = holder2;
	newholder3 = holder3;
	printf("in routeaddroutine \n");
	nullhandler = find_vertex(graphtohandle, holder1);
	nullhandler1 = find_vertex(graphtohandle, holder1);

	if(nullhandler != NULL && nullhandler1 != NULL){
		add_edge_undirected(graphtohandle, newholder1, newholder2, newholder3);
		printplusok1(sd);
		write(sd,routeadded1,strlen(routeadded1));
		printendpulse(sd);

	}
     
	else{
		printminuserror(sd);
	}

}

void RouteDeleteRoutine(int sd, int holder1, int holder2){
	int newholder1,newholder2;
	char *routedelete = "Route deleted.";
	newholder1 = holder1;
	newholder2 = holder2;

	printf("in RouteDeleteRoutine \n");
	edgey = get_edge(graphtohandle, newholder1, newholder2);

	if(edgey != NULL ){
		remove_edge(graphtohandle, newholder1, newholder2);
		
		remove_edge(graphtohandle, newholder2, newholder1);
		printplusok1(sd);
		write(sd,routedelete,strlen(routedelete));
		printendpulse(sd);
	}
	else{
		printminuserror(sd);
	}
}

void RouteShowroutine(int sd, int holder1){
	int count = 0; 
	char num[256];
	int i;
	
	nullhandler = find_vertex(graphtohandle,holder1);


    if(nullhandler != NULL){
	edgey2 = get_edges(graphtohandle,nullhandler,&count);

    edgey3 = *edgey2;

    printplusok1(sd);
	sprintf(num,"%d",count);	
	write(sd,num,strlen(num));
	printendpulse(sd);


	for(i=0; i<count ; i++){
	
	sprintf(num,"%d",(edgey3->vertex->id));
	write(sd,num,strlen(num));
	printendpulse(sd);
	edgey3 = *(edgey2 + 1);
	}
	
	}
	else{
		printminuserror(sd);
	}


	
}


void RouteHopRoutine(int sd, int holder1,int holder2){
	int newholder1,newholder2;
	char *nexthop1 = "Next HOP -> ";
	char num[256];
	
	int count = 0;
	int i=0;
	int idholder;
	
	newholder1 = holder1;
	newholder2 = holder2;
	

	nullhandler = find_vertex(graphtohandle,newholder1);
    nullhandler1 = find_vertex(graphtohandle,newholder2);
	if(((nullhandler != NULL) || (nullhandler1 != NULL )) && (newholder1 != newholder2)){
		printplusok1(sd);

		

		array = dijkstra(graphtohandle,holder1,&count);
		array = &array[holder2];
		idholder = array->next_hop;
		sprintf(num,"%d",idholder );
		write(sd,num,strlen(num));
		printendpulse(sd);
	
	}

	else{
		printminuserror(sd);
	}
	
	}

void RouteTableRoutine(int sd, int holder1){
	int count = 0;
	int count1 = 0;
	int vertexholder= 0;
	int Idholder;
	double Weight;
	int *pointertoverticies;
	char num[256];
	int i;
	char *arrow = " -> ";
	char *weight = ", weight ";
	char *nextyhop = ", next-hop ";
	char *INF = "INF";

	pointertoverticies = get_vertices(graphtohandle,&count1);
	
	array = dijkstra(graphtohandle,holder1,&count);	
	printplusok1(sd);
	sprintf(num,"%d",count-2);
	write(sd,num,strlen(num));
	printendpulse(sd);

	for(i=0;i<count1;i++){
		
		vertexholder = pointertoverticies[i];
		array2 = &array[vertexholder];
		Idholder = array2->next_hop;
		Weight = array2->weight;
		if(vertexholder == holder1){
			continue;
		}
		sprintf(num,"%d",holder1 );
		write(sd,num,strlen(num));
		
		write(sd,arrow,strlen(arrow));

		sprintf(num,"%d", vertexholder);
		write(sd,num,strlen(num));
		
		write(sd,nextyhop,strlen(nextyhop));
		sprintf(num,"%d", Idholder);

		write(sd,num,strlen(num));
		write(sd,weight,strlen(weight));
		if(Weight > 10000){
			write(sd,INF,strlen(INF));

		}
		else{
		sprintf(num,"%0.2f",Weight);
		write(sd,num,strlen(num));
		}
		printendpulse(sd);
	}

	
	
	
	
}


void printplusok(int sd){
	char *plusok = "+OK\r\n";
 
	write(sd,plusok, strlen(plusok));
}	

void printplusok1(int sd){
	char *plusok = "+OK ";
 
	write(sd,plusok, strlen(plusok));
}	

void printendpulse(int sd){
	char *endpulse = "\r\n";
 
	write(sd,endpulse, strlen(endpulse));
}	

void printminuserror(int sd){
	char *MinusErr = "-ERR\r\n";
	write(sd,MinusErr, strlen(MinusErr));
}	

void ReadLineFromNetwork(int sd, char *buf, int size)
{
	size_t n;
	char c;
	int i = 0;
	int cline = 0;
	do
	{
		n = read(sd, &c, 1);
		buf[i] = c;
		
		if( i > 0 && buf[i] == '\n' && buf[i-1] == '\r')
		{
			buf[i-1] = 0;
			cline = 1;
			break;
		}
		i++;
	}	while(cline == 0);
}





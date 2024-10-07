/*
 *  dijkstra.c
 *  COMP1006 Large Coursework 02
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <float.h>
#include "graph.h"
#include "dijkstra.h"

int list_is_empty(int *array,int biggest);
int get_biggest_Id(Graph *graph);
int * makes_S_array(Graph*graph,int id);
double * makes_D_array(Graph *graph,int id);
int * makes_R_array(Graph *graph,int id);
double smallest_num_between_s_and_d(Graph * graph, int *s_array,double *d_array,int *idwheresmallestbe);
int in_s_array(int *s_array,int v,int biggest);


/* find shortest paths between source node id and all other nodes in graph. */
/* upon success, returns an array containing a table of shortest paths.  */
/* return NULL if *graph is uninitialised or an error occurs. */
/* each entry of the table array should be a Path */
/* structure containing the path information for the shortest path between */
/* the source node and every node in the graph. If no path exists to a */
/* particular desination node, then next should be set to -1 and weight */
/* to DBL_MAX in the Path structure for this node */
Path *dijkstra(Graph *graph, int id, int *pnEntries)
{
    Path *table =NULL;
    Vertex *vertex;
    LinkedList *Listofedges;
    Node *nodeforedge;
    Edge *currentedge;
    int empty;
    int cost;
    int *s_array;
    double *d_array;
    int *R_array;
    int v;

    int i;
    double smallest;
    int biggest;
    int idwheresmallestbe = 0;

    if(!graph){
        
        fprintf(stderr,"Error:graph doesnt exist");
        return NULL;
    }
    vertex = find_vertex(graph, id);
    
    if(vertex == NULL){
        fprintf(stderr,"Error;graph doesnt exist");
        return NULL;
    }

    
    s_array = makes_S_array(graph,id);  /*done*/

    d_array = makes_D_array(graph,id);
    R_array = makes_R_array(graph,id);

    biggest = get_biggest_Id(graph);
    biggest++;
    
    table = (Path *)calloc(biggest,sizeof(Path));
    

  
    

    


    
    empty = list_is_empty(s_array,biggest);
    while(empty == 0){
        smallest = smallest_num_between_s_and_d(graph,s_array,d_array,&idwheresmallestbe);
        

        if(smallest == DBL_MAX){
            
            break;
        }

        s_array[idwheresmallestbe] = 0;
        empty = list_is_empty(s_array,biggest);

        vertex = find_vertex(graph,idwheresmallestbe);
        if(vertex== NULL){
            break;
        }
        Listofedges = vertex->edges;
        nodeforedge = Listofedges-> head;
        while(nodeforedge){
            currentedge = nodeforedge->data;
            if(currentedge){

                v = currentedge->vertex->id;
                if(in_s_array(s_array,v,biggest) == 1){

                    cost= d_array[idwheresmallestbe] + currentedge->weight;

                    if(cost < d_array[v]){
                        R_array[v] = R_array[idwheresmallestbe];
                        d_array[v] = cost;
                    }
                }



            }
            nodeforedge = nodeforedge->next;

        }
        


    }
/*REMOVE AFTER */
    
  
 
  

  
    
/*REMOVE ME */

    
    
    /* Insert your implementation of Dijkstra's algorithm here */
    
   
    for(i = 0; i<biggest; i++){
        table[i].next_hop = R_array[i];
        table[i].weight = d_array[i];
    }

    
    table[id].next_hop = -1;
    table[id].weight = DBL_MAX;
    
    
    *pnEntries = biggest;

    free(d_array);
    free(s_array);
    free(R_array);
    return table;
}


int in_s_array(int *s_array,int v,int biggest){
    int i;

    for(i= 0 ; i<biggest; i++){
     if(s_array[i] == v){
        return 1;
     }

    }
    return 0;
    

}

int get_biggest_Id(Graph *graph){
    int count = 0;
    int *ptr, i , holder, biggest;
    ptr = get_vertices(graph, &count);
    for(i = 0;i<count; i++){
        if(i == 0){
            biggest = ptr[i];
        }
        holder = ptr[i];
        if(holder > biggest){
            biggest = holder;
        }
        
        /*to see whats in the array but all works remove print later on*/
        
    }
    
    free(ptr);
    return biggest;

}


double * makes_D_array(Graph *graph,int id){
    Vertex *vertex;
    Edge *edge;
    Edge **edgey;
    int count;
    int i=0,z = 0;
    double *d_array;
    int biggest;

    biggest = get_biggest_Id(graph);
    biggest++;
    vertex = find_vertex(graph,id);
    if(!(d_array = (double *)calloc(biggest,sizeof(double)))){
        fprintf(stderr,"ERROR;COULD NOT MAKE ARRAY");
        exit(EXIT_FAILURE);
    }

    edgey = get_edges(graph,vertex,&count);
    edge = *edgey;
    for(i= 0;i<biggest; i++){
        d_array[i] = DBL_MAX;
        for(z = 0; z <count; z++){

        if (edge->vertex->id == i){
            d_array[i] = edge->weight;
            
        }
        edge = *(edgey + z);
        
        }
    }
    free(edgey);
    return d_array;
   
}

int list_is_empty(int *array,int biggest){
    int i;
    int count =0; 
    
    
    for(i= 0 ; i<biggest; i++){
        if(array[i]== 0){
            count++;
        }
        if(count == biggest){
            return 1;
        }
    }
    return 0;

}

int * makes_S_array(Graph *graph, int id){
    int biggest;   
    int *s_array;
    int i, z;
    int count;
    int *ptr;

    biggest = get_biggest_Id(graph);
    
    


    biggest++;
    s_array = (int *)calloc(biggest,sizeof(int));
    ptr = get_vertices(graph, &count);
    for(i= 0; i<biggest;i++){
        if(i == id){
            continue;
        }
        for(z = 0; z<count; z++){
            
            if(i == ptr[z]){
             s_array[i] = ptr[z];
            }
        }
        
    }

    
    free(ptr);
    return s_array;
}

int * makes_R_array(Graph *graph,int id){
    Vertex *vertex;
    Edge *edge;
    Edge **edgey;
    
    int * R_array;
    int count;
    int i=0,z = 0;
    int biggest;

    biggest = get_biggest_Id(graph);
    
    biggest++;
    
    vertex = find_vertex(graph,id);

    R_array = (int *)calloc(biggest,sizeof(int));

    edgey = get_edges(graph,vertex,&count);
    edge = *edgey;
    for(i= 0;i<biggest; i++){
        R_array[i] = -1;
        for(z = 0; z <count; z++){

        if (edge->vertex->id == i){
            R_array[i] = edge->vertex->id;
            
        }
        edge = *(edgey + z);
        
        }
    }

   
    free(edgey);
    return R_array;
}


double smallest_num_between_s_and_d(Graph * graph, int *s_array,double *d_array,int *idwheresmallestbe){
    double smallest = DBL_MAX;
    double holder;
    int i;
    int biggest;
    biggest = get_biggest_Id(graph);
    biggest++;

    for(i=0;i<biggest ; i++){
        if(s_array[i] == 0){
            continue;
        }
        holder = d_array[i];

        if(holder < smallest){
            
            smallest = holder;
            *idwheresmallestbe = i;
        }
    }
    return smallest;

}


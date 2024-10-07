#include "graph.h"

#include <stdio.h>
#include <stdlib.h>

/* initialise an empty graph */
/* return pointer to initialised graph */
Graph *init_graph(void)
{
    Graph *graph; 
    graph = initialise_linked_list();
    return graph;

}

/* release memory for graph */
void free_graph(Graph *graph)
{
    Node *nodetouse;
    Vertex *vertextobeused;

    if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist cant free graph\n");
        return;
    }
    nodetouse = graph->head;
    while(nodetouse){
        if(nodetouse->data){
        vertextobeused = (Vertex *)nodetouse->data;
        free_vertex(vertextobeused);
        }
        nodetouse = nodetouse->next;
    }

    free_linked_list(graph);
    
}

/* initialise a vertex */
/* return pointer to initialised vertex */
Vertex *init_vertex(int id)
{
    Vertex *vertex ;
    if(!(vertex = (Vertex *)malloc(sizeof(Vertex)))){
        fprintf(stderr, "error;unable ");
        exit(EXIT_FAILURE);
    }
    vertex->id = id;
    vertex->edges = initialise_linked_list();

    return vertex; 
}

/* release memory for initialised vertex */
void free_vertex(Vertex *vertex)
{
    LinkedList *currentlist;
    Edge *edge;

    Node *node;

    if(!vertex){
        fprintf(stderr, "Warning: the vertex doesnt exist cant free vertex\n");
        return;
    }
    
    currentlist = vertex->edges;
    node = currentlist->head;
    if(vertex->edges){

    while(node){
        if(node->data){
            edge = (Edge *)node->data;
            free_edge(edge);
        }
        
        node = node->next;
    }
    
    free_linked_list(currentlist);
    }
    free(vertex);
    

}

/* initialise an edge. */
/* return pointer to initialised edge. */
Edge *init_edge(void)
{
    Edge *edge;
    
    if(!( edge = (Edge *)malloc(sizeof(Edge)))){    
        fprintf(stderr, "error;unable ");
        exit(EXIT_FAILURE);
    }

    edge->weight = 0.00;
    edge->vertex = NULL;

    return edge; 

}

/* release memory for initialised edge. */
void free_edge(Edge *edge)
{
    if(!edge){
        fprintf(stderr, "Warning: the graph doesnt exist cant free edge\n");
        return;
    }
    free(edge);
}

/* remove all edges from vertex with id from to vertex with id to from graph. */
void remove_edge(Graph *graph, int from, int to)
{
   
    Edge *edgetoremove;
    Node *node;

     if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist cant remove edge\n");
        return;
    }

    else{
        
        edgetoremove = get_edge(graph,from,to);
        

        if(edgetoremove){
            node = find_vertex(graph,from)->edges->head;

            
            while(node){
                if((Edge *)node->data == edgetoremove)
                {
                    node->data = NULL;
                }
                node = node->next;

            }

            free_edge(edgetoremove);
        }

    }
}

/* remove all edges from vertex with specified id. */
void remove_edges(Graph *graph, int id)
{
    Vertex *vertex;
    Edge *edge;
    LinkedList *currentedgelist;
    Node *nodetomovethroughlist;
    

    if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist cant remove edge\n");
        return;
     }
    
    else{
        vertex = find_vertex(graph, id);
        if(!vertex){
            return;
        }
        if(!vertex->edges){
            return;
        }
        currentedgelist = vertex->edges;
        nodetomovethroughlist = currentedgelist->head;
        


        while(nodetomovethroughlist){
            if(nodetomovethroughlist->data){
                edge = (Edge *)nodetomovethroughlist->data;
                remove_edge(graph,id,edge->vertex->id);
               
            }

            nodetomovethroughlist = nodetomovethroughlist->next;
        }
        
        }

    
}

/* output all vertices and edges in graph. */
/* each vertex in the graphs should be printed on a new line */
/* each vertex should be printed in the following format: */
/* vertex_id: edge_to_vertex[weight] edge_to_vertex[weight] ... */
/* for example: */
/* 1: 3[1.00] 5[2.00] */
/* indicating that vertex id 1 has edges to vertices 3 and 5 */
/* with weights 1.00 and 2.00 respectively */
/* weights should be output to two decimal places */
void print_graph(Graph *graph)
{
    Node *node;
    Node *edgesnode;
    Vertex *vertex;
    Edge *edge;
    


    if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist print graph\n");
        return;
    }

    node = graph->head;
    while(node){
        vertex = node->data;

        printf("%d:",vertex->id);
        edgesnode = vertex->edges->head;
        while(edgesnode){
            
            edge = edgesnode->data;
            if(edge){
                printf(" %d [%.2f]",edge_destination(edge),edge_weight(edge));
            }
            
            edgesnode = edgesnode->next;

        }
        printf("\n");
        

        node = node->next;

    }



    

    

}

/* find vertex with specified id in graph. */
/* return pointer to vertex, or NULL if no vertex found. */
Vertex *find_vertex(Graph *graph, int id)
{
    Node *travel;
    Vertex *vertex;
    
    if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist cant find vertex\n");
        return NULL;
    }
    
    travel = graph->head;
    
    while(travel){
        if(travel->data){
            vertex = (Vertex *)travel->data;

            if(id == vertex->id){
                return vertex;
            }
        }
        travel = travel->next;
        
    }
    return NULL;
    
}

/* create and add vertex with specified id to graph. */
/* return pointer to vertex or NULL if an error occurs. */
/* if vertex with id already exists, return pointer to existing vertex. */
Vertex *add_vertex(Graph *graph, int id)
{
    Vertex *vertex;
    if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist cant add vertex \n");
        return NULL;
    }
    if(find_vertex(graph,id) != NULL){
        vertex = find_vertex(graph,id);
        return vertex;
    }

    vertex = init_vertex(id);
    append_linked_list(graph,vertex);
    return vertex;

}

/* remove vertex with specified id from graph. */
/* remove all edges between specified vertex and any other vertices in graph. */
void remove_vertex(Graph *graph, int id)
{
    Vertex *vertex;
    Node *node;
    int i,j,k;
    i = 1;
    j=1;
    k =1;
    i = j+k;
    j = i+ 2;
    

    if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist cant remove vertex\n");
        return;
    }

    else{
        vertex = find_vertex(graph,id);
        if(vertex){
            node = graph->head;
            while(node){
                if((Vertex *)node->data == vertex){
                    node->data = NULL;
                }
                node = node->next;
            }
            free_vertex(vertex);
        }
        
 
    }
}

/* add directed edge with specified weight between vertex with id from */
/* to vertex with id to. */
/* if no vertices with specified ids (from or to) exist */
/* then the vertices will be created. */
/* multiple vertices between the same pair of vertices are allowed. */
/* return pointer to edge, or NULL if an error occurs found. */
Edge *add_edge(Graph *graph, int from, int to, double weight)
{
    
    Edge *edge;
    Vertex *vertex;
    Vertex * vertex1;
    
    if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist cant Add edge\n");
        return NULL; 
    }
    vertex = find_vertex(graph,from);
    if(vertex ==NULL){
        vertex = add_vertex(graph,from);
    }
    vertex1 = find_vertex(graph,to);
    if(vertex1 ==NULL){
        vertex1 = add_vertex(graph,to);
    }
    edge = init_edge();
    edge ->weight = weight;
    edge ->vertex = vertex1;
    append_linked_list((LinkedList *)vertex->edges,edge);
    return edge;
    
}

/* add two edges to graph, one from vertex with id from to vertex with id to, */
/* and one from vertex with id to to vertex with id from. */
/* both edges should have the same weight */
/* if no vertices with specified ids (from or to) exist */
/* then the vertices will be created. */
/* multiple vertices between the same pair of vertices are allowed. */
void add_edge_undirected(Graph *graph, int from, int to, double weight)
{
    
    if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist cant Add edge\n");
        return;
    }

    add_edge(graph,from,to,weight);
    add_edge(graph,to,from,weight);
}

/* return array of node ids in graph. */
/* array of node ids should be dynamically allocated */
/* set count to be the number of nodes in graph */
/* return NULL if no vertices in graph */
int *get_vertices(Graph *graph, int *count)
{
    Node *node;
    
    int *arrayofint;
    int i = 0;

    node = graph->head;

    if(!node){
        return NULL;
    }

    while(node){
        
        
        if(node->data){
            i++;
        }
        node = node->next;
    }
    node = graph->head;
    arrayofint= (int *)calloc(i,sizeof(int));
    *count = i;
    i= 0;
    while(node){
        if(node->data){
            arrayofint[i] = ((Vertex *)node->data)->id;
        }
        i++;
        node =node ->next;

    }

    return arrayofint;
}

/* return array of pointers to edges for a given vertex. */
/* array of edges should be dynamically allocated */
/* set count to be number of edges of vertex */
/* return NULL if no edges from/to vertex */
Edge **get_edges(Graph *graph, Vertex *vertex, int *count)
{
    Edge **edges;
    
    Node *node;
    int i = 0;
    if(!graph){
        return NULL;
    }
    if(!vertex){
        return NULL;
    }
    if(!vertex->edges->head){
        return NULL;
    }

    node = vertex->edges->head;

    
    while(node){ 
        if(node->data){
            i++;

        }
        node = node->next;   

    }
    if(i == 0){
        return NULL;
    }
    *count = i;
    
    edges = (Edge **)calloc(i,sizeof(Edge *));
    i= 0;
    node = vertex->edges->head;
    while(node){
        if(node->data){
            edges[i]= (Edge *)node->data;
            i++;
            
        }
        node =node->next;


    }

    return edges;
    
}

/* return pointer to edge from vertex with id from, to vertex with id to. */
/* return NULL if no edge */
Edge *get_edge(Graph *graph, int from, int to)
{
    Edge *edge = NULL;
    Vertex *vertex;
    Node *travel;
    LinkedList *listtouse;

    if(!graph){
        fprintf(stderr, "Warning: the graph doesnt exist cant get edge\n");
        return NULL;

    }

    vertex = find_vertex(graph,from);

    listtouse = vertex->edges;

    travel = listtouse->head;


    while(travel){
        if(travel->data){

        
        edge = (Edge *)travel->data;
        if(edge->vertex->id == to){


            return edge;
        }
        }
        travel = travel->next;

    }
    
/*
    while(travel){

        edge = travel->data;

        if(edge->vertex->id == to){

            return edge;
        }

        travel = travel->next;
    }
*/

    return NULL;
}


/* return id of destination node of edge. */
int edge_destination(Edge *edge)
{
    int iddes;
    iddes = edge->vertex->id;
    return iddes;
}

/* return weight of edge. */
double edge_weight(Edge *edge)
{
    double weight1;
    weight1 = edge->weight;
    return weight1;

}
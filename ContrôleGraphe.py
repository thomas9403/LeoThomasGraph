import random
from typing import Set, Tuple



def create_random_graph(is_oriented:bool,is_waighted:bool,nb_edges:int,nb_vecters:int)->Set[Tuple[int,int,int]]:
    if is_oriented:
        graphe = set()
        while len(graphe) < nb_edges:
            graphe.add((random.randrange(nb_vecters),random.randrange(nb_vecters),random.randrange(100)if is_waighted else 1))
        file = open("graph.txt", "w")
        file.write(str(graphe))
        file.close()
        return graphe



def dominatingSet(graph):
    print(graph)
    s = []
    visited = []
    #convertir le graph en liste
    graph = list(graph)
    if len(graph) != len(visited):
        sommet = random.randint(0, len(graph)-1)
        print("On choisit un sommet aléatoire : ", sommet)
        if(graph[sommet] not in visited):
            #ajouter un sommet sauf si c'est une parenthèse, une virgule, un espace ou une accolade
            if graph[sommet] != "(" and graph[sommet] != ")" and graph[sommet] != "," and graph[sommet] != " " and graph[sommet] != "{":
                s.append(graph[sommet])
                visited.append(graph[sommet])
                print("On ajoute le sommet : ", graph[sommet])
                for i in range(len(graph)):
                    if(graph[i] not in visited):
                        visited.append(graph[i])
                        print("On ajoute le sommet : ", graph[i])
    return s
    
    
graph = create_random_graph(True,True,1000, 15000)
print(dominatingSet(graph))
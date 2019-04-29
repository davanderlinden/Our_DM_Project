#like independence, start with n instead of n-1

import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

G = nx.read_edgelist('graph_library\pan.txt')

def is_clique(G,s):
    for v in s:
        L = list(s)
        L.remove(v)
        for w in L:
            if w not in list(neighbors(G,v)):
                return False
    return True
    
def maximum_clique_set(G):
    n = len(V(G))
    for k in range(n,1,-1):
        for s in combinations(V(G),k):
            if is_clique(G,list(s)) == True:
                return list(s)
            

def is_matching(G,s):
    
    for i in s:
        if len(s[i]) != 2:
            return print("Not every part of the set is an edge.")
        else:
            if s[i][0] not in list(neighbors(G,s[i][1])):
                return print("One or more of your pairs of vertices are not edges.")
    
    L = []
    for sublist in s:
        for item in sublist: 
            L.append(item)
    M = list(set(L))
    M.sort()
    L.sort()
    if L == M:
        return True
    else:
        return False
    
A = [('a','b'),('a','e')]
B = [('a','b'),('c','e')]
C = [('a','b','c'),('a','b')]
D = [('a','c'),('a','b')]
print(is_matching(G,B))
                

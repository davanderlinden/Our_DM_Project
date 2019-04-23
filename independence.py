import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

G = nx.read_edgelist('graph_library\pan.txt')

def is_independent(G,s):
    for v in s:
        if list(set(s) & set(neighbors(G,v))) != []:
            return False
    return True

def maximum_independent_set(G):
    n = len(V(G))
    for k in range(n-1,1,-1):
        for s in combinations(V(G),k):
            if is_independent(G,list(s)) == True:
                return list(s)
            
def independence_number(G):
    return len(maximum_independent_set(G))




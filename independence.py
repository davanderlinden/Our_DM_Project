# -*- coding: utf-8 -*-

import networkx as nx
from itertools import combinations
from functions.global_properties import V
from functions.local_properties import neighbors

def is_independent(G,S):
    for s in S:
        A = list(neighbors(G, s))
        for a in A:
            if a in S:
                return False
    return True
            
        
def max_independent_set(G):
    n = len(V(G))
    for k in range(n-1,1,-1):
        for S in combinations(V(G),k):
            if is_independent(G,list(S)) == True:
                return list(S)
            
def independence_number(G):
    return len(max_independent_set(G))




def is_independent_spes(G,S,v):
    for s in S:
        A = list(neighbors(G, s))
        for a in A:
            if a in S:
                return False
            if v not in S:
                return False
            
    return True

def independent_set(G,v):
    n = len(V(G))
    for k in range(n-1,1,-1):
        for S in combinations(V(G),k):
            if is_independent_spes(G,list(S),v) == True:
                return list(S)

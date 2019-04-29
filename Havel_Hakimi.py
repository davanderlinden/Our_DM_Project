import networkx as nx
from functions.global_properties import degree_sequence

def delete_first_term(L):
    L.pop(0)
    return None

def Havel_Hakimi_derivative(L):
    d_1 = L[0]
    L.pop(0)
    for i in range(d_1):
        L[i]-=1
    L.sort(reverse=True)
    return None

def Havel_Hakimi_process(L, show=False):
    assert len(L)!=0, 'List cannot be empty'
    if show == True:
        print(L)
    while L[0] > 0:
        Havel_Hakimi_derivative(L)
        if show == True:
            print (L)
    return None

def is_graphic(L):
    Havel_Hakimi_process(L)
    return sum(L)==0

def residue(G):
    L = degree_sequence(G)
    Havel_Hakimi_process(L)
    return len(L)

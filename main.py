import networkx as nx
import numpy as np
from functions.global_properties import *
from functions.local_properties import *
from independence import *

G = nx.read_edgelist('graph_library\pan.txt')

A = [('m','i','n','d','y'),('d','o','o')]
B = ['m','i','n','d','y','y']

for i in range(0,1,1) in A:
    print(A[i])


'''
for v in B:
    L = list(B)
    L.remove(v)
    print(L)
'''
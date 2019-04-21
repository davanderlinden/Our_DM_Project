import networkx as nx

from functions import * 

g = nx.read_edgelist("G.txt",create_using=nx.DiGraph(), nodetype=int)

a = degree(g)
print(a)

import networkx as nx

"""
	Functions file for graph theory
"""

def is_matching(G, Matching):
	"""
		Determines if given graph is matching to given matching params
		Returns Boolean
	"""
	if not G and not Matching:
		raise Exception("Please provide Graph and Matching params")
	return nx.is_matching(G, Matching)

def matching(G):
	if not G:
		raise Exception("Please provide Graph value")
	return nx.maximal_matching(G)

def independent_numbers(G, nodes=None, seed=None):
	if not G:
		raise Exception("You must provice path graph value")
	if nx.is_directed(G):
		C = G.to_undirected()

	else:
		C = G
	return nx.maximal_independent_set(C, nodes=None, seed=None)

def radius(G, e=None, usebounds=False):
	if not G:
		raise Exception("Please provide graph value")
	return nx.radius(G, e=None, usebounds=False)

def diameter(G, e=None, usebounds=False):
	if not G:
		raise Exception("Please provide graph value")
	return nx.diameter(G, e=None, usebounds=False)

def degree(G):
	return sorted([d for n, d in G.degree()], reverse=True)

def max_degree(G):
	if not G:
		raise Exception("Please provide graph value")
	dgr = degree(G)
	return max(dgr)

def min_degree(G):
	if not G:
		raise Exception("Please provide graph value")
	dgr = degree(G)
	return min(dgr)

def average_degree(G):
	if not G:
		raise Exception("Please provide graph value")
	dgr = degree(G)
	avg = sum(dgr) / float(len(dgr))
	return avg

def greedy_coloring(G):
	if not G:
		raise Exception("Please provide graph value")
	C = nx.cycle_graph(G)
	d = nx.coloring.greedy_color(C, strategy='largest_first')
	return d

def clique_numbers(G):
	if not G:
		return Exception("Please provide graph value")

	if nx.is_directed(G):
		C = G.to_undirected()

	else:
		C = G

	cn = nx.find_cliques(C)
	data = []
	for i in cn:
		if i is not None:
			data.append(i)
		next(cn)
	return data

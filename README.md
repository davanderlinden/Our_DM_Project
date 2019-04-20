# Our_DM_Project
group project 
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

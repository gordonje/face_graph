import networkx as nx
from networkx.readwrite import json_graph
import json
import matplotlib.pyplot as plt

print '    Reading in .gml file...'

g = nx.read_gml("my_facebook_network.gml.txt")

print '''James' social graph contains {nodes} friends with {edges} connections.'''.format(
								  nodes = g.number_of_nodes()
								, edges = g.size()
								)

# print "The density of the graph is {}.".format(nx.density(g))

# print '   Finding cliques...'

# max_clique_len = nx.graph_clique_number(g)

# print "The biggest clique contains {} friends.".format(max_clique_len)

# biggest_cliques = []

# for clique in nx.find_cliques_recursive(g):
	
# 	if len(clique) == max_clique_len:

# 		big_clique = []

# 		for i in clique:

# 			big_clique.append(g.node[i])

# 		biggest_cliques.append(big_clique)

# print "There are {0} cliques with {1} friends".format( len(biggest_cliques), max_clique_len)

# for clique in biggest_cliques:
# 	print '    This one includes:'

# 	for node in clique:
# 		print '        ' + node['label']

print '    Calculating degree centrality for nodes...'

deg_cent = nx.betweenness_centrality(g)

for key, value in deg_cent.iteritems():
	g.node[key]['deg_cent'] = value

print '    Calculating betweeness centrality for nodes...'

bw_cent = nx.betweenness_centrality(g)

for key, value in bw_cent.iteritems():
	g.node[key]['bw_cent'] = value

print '    Calculating eigenvector centrality for nodes...'

ev_cent = nx.eigenvector_centrality(g)

for key, value in ev_cent.iteritems():
	g.node[key]['ev_cent'] = value

for i in g.nodes(data=True):
	if i[1]['deg_cent'] != i[1]['bw_cent']:
		print i

print '    Writing .json file...'

d = json_graph.node_link_data(g) # node-link format to serialize

json.dump(d, open('viz/data/force.json','w'))


# nx.draw_networkx(g, with_labels = True)

# plt.savefig("graph.png")

# plt.show()


# 'adj_matrix',
#  'adjacency_matrix',
#  'adjacency_spectrum',


# 'average_clustering',
#  'average_degree_connectivity',
#  'average_neighbor_degree',
#  'average_node_connectivity',
#  'average_shortest_path_length',


# 'betweenness',
#  'betweenness_centrality',
#  'betweenness_centrality_source',
#  'betweenness_centrality_subset',
#  'betweenness_subset',

# 'centrality',

# 'cluster',
#  'clustering',

# 'eccentricity',
#  'edge_betweenness',
#  'edge_betweenness_centrality',
#  'edge_betweenness_centrality_subset',
#  'edge_boundary',
#  'edge_connectivity',
#  'edge_current_flow_betweenness_centrality',
#  'edge_current_flow_betweenness_centrality_subset',
#  'edge_load',
#  'edgelist',
#  'edges',
#  'edges_iter',
#  'ego',
#  'ego_graph',
#  'eigenvector',
#  'eigenvector_centrality',
#  'eigenvector_centrality_numpy',

print 'fin'


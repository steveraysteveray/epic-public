import os
import fnmatch
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout


def getBaseURIFromFile(f):
	first_line = f.readline().split(": ")
	if first_line[0] == "# baseURI":
		baseURI = first_line[1][:-1]
		return baseURI
	else:
		# print "No baseURI found."
		pass

def getImportURIFromFile(f):
	is_importing      = True
	import_ontologies = []
	f.readline()
	while is_importing:
		line = f.readline().split(": ")
		if line[0] == "# imports":
			import_ontologies.append(line[1][:-1])
		else:
			is_importing = False
	return import_ontologies

def getBaseAndImportURIFromFile(path):
	f = open(path)
	is_importing      = True
	import_ontologies = []
	first_line = f.readline().split(": ")
	if first_line[0] == "# baseURI":
		baseURI = first_line[1][:-1]
	while is_importing:
		line = f.readline().split(": ")
		if line[0] == "# imports":
			import_ontologies.append(line[1][:-1])
		else:
			is_importing = False
	f.close()
	return baseURI, import_ontologies

def findFilesToImport(kp_path, importURI):
	matches = []
	for root, dirnames, filenames in os.walk(kp_path):
		for filename in fnmatch.filter(filenames, '*.ttl'):
			f = open(os.path.join(root, filename))
			if getBaseURIFromFile(f) == importURI:
				matches.append(os.path.join(root, filename))
			f.close()
	return matches

def parseFileNameFromPath(path):
	return path.split("\\")[-1]

# f = open("SCHEMA_KP_EPIC_building-v1.0.ttl")
# baseURI = getBaseURIFromFile(f)
# imports = getImportURIFromFile(f)
# print findFilesToImport(path, imports[0])
# print
# print

path = '..\\..\\'
explored = []
G = nx.DiGraph()

def buildTree(root_path, depth=0):
	print parseFileNameFromPath(root_path)
	if root_path is None or depth>=1000:
		return None
	baseURI, importURI = getBaseAndImportURIFromFile(root_path)
	explored.append(root_path)
	for import_ont in importURI:
		child_path = findFilesToImport(path, import_ont)
		if len(child_path) > 0:
			if child_path[0] not in explored:
				fname = parseFileNameFromPath(root_path)
				G.add_edge(fname, parseFileNameFromPath(child_path[0]))
				G.node[fname]["filepath"] = root_path
				G.node[fname]["URI"] = baseURI
				buildTree(child_path[0], depth+1)
			else:
				G.add_edge(parseFileNameFromPath(root_path), parseFileNameFromPath(child_path[0]))
				print child_path[0], " is already in ", root_path


buildTree("SCHEMA_KP_EPIC_building-v1.0.ttl")

nx.draw(G, with_labels=True)
plt.show()

a = nx.nx_agraph.to_agraph(G)
a.layout('dot', args='-Nfontsize=12 -Nwidth=".2" -Nheight=".2" -Nmargin=0 -Gfontsize=8')
a.draw('ontology_hierarchy.png')

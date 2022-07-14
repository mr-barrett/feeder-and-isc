import feeder
from feeder import *

import cairo
from cairo import *

import igraph
from igraph import *

'''DP2_feeder = feeder(8,"AL","750",220)
print(outputISC(119048,208,DP2_feeder))'''


g = Graph()
g.add_vertices(6)
g.add_edges([(0,1),(0,2),(0,3),(0,4),(1,5)])

names = list()
names = ["MDP","H1","H2","A","LS","H1A"]

currents = list()
currents = [42000,40000,30000,20000,10000,5555]

g.vs["isc"] = currents
g.vs["ID"] = names

g.add_vertex(ID="H2A",isc=69420)


######  Don't make anymore vertices or edges ###############
labels = list()
if len(g.vs["isc"]) == len(g.vs["ID"]):
    for i in range(len(g.vs["ID"])):
        labels.append(f"Panel: {g.vs[i]['ID']}\nIsc: {g.vs[i]['isc']}") 
g.vs["label"] = labels

summary(g)

style = {}
style["vertex_size"] = 20
style["edge_width"] = 2
style["vertex_color"] = "#25f355"
style["bbox"] = (500,500)
style["margin"] = 100
style["layout"] = g.layout("tree")

mar = 100

igraph.plot(g, **style)
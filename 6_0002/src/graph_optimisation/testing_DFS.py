from constructing_graph import buildCityGraph
from depth_first_search import shortestPath
from graph_opt_types import Digraph, Node,  Edge
from printPath import printPath  


def test_dept_first_search(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to', destination, 'is', printPath(sp))

    else:
        print('There is no path from', source, 'to', destination)

test_dept_first_search('Boston', 'Chicago')
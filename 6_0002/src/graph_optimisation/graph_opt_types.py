
class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination 
    def getSource(self):
        return self.source
    def getDestination(self):
        return self.destination
    def __str__(self):
        return self.source.getName()+ '->' + self.destination.getName()

class Digraph(object):
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node]=[]
    def addEdge(self, edge):
        source = edge.getSource()
        destination = edge.getDestination()
        if not (source in self.edges and destination in self.edges):
            raise ValueError('Node not in graph')
        self.edges[source].append(destination)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n 

    def __str__(self):
        result = ''
        for source in self.edges:
            for destination in self.edges[source]:
                result = result + source.getName() + '->'+ destination.getName() + '\n'
        return result[:-1] #omit final newline 


class graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


    


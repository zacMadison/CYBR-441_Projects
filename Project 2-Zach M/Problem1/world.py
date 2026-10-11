from node import Node
from graph import Graph


class World:

    graph = None
    def __init__(self, num):
        #num is how many cells
        g = Graph()
        #in here, create your nodes
        #connect them to each other
        #and add them to the graph
        #object.  This will run in 
        #the "main" of "interface.py"
            # Create Nodes
        n1 = Node(img="Vac-L-Tr-LR.png", nodeId = 1, trash=[1, 1], vac="Left")
        n2 = Node(img="Vac-L-Tr-R.png", nodeId = 2, trash=[0, 1], vac="Left")
        n3 = Node(img="Vac-L-Tr-L.png", nodeId = 3, trash=[1, 0], vac="Left")
        n4 = Node(img="Vac-L-Tr-N.png", nodeId = 4, trash=[0, 0], vac="Left")
        n5 = Node(img="Vac-R-Tr-LR.png", nodeId = 5, trash=[1, 1], vac="Right")
        n6 = Node(img="Vac-R-Tr-R.png", nodeId = 6, trash=[0, 1], vac="Right")
        n7 = Node(img="Vac-R-Tr-L.png", nodeId = 7, trash=[1, 0], vac="Right")
        n8 = Node(img="Vac-R-Tr-N.png", nodeId = 8, trash=[0, 0], vac="Right")
            # Create connections
        
        n1.addConnection(n2, "suck")
        n1.addConnection(n5, "move")
        n2.addConnection(n2, "suck")
        n2.addConnection(n6, "move")
        n3.addConnection(n4, "suck")
        n3.addConnection(n7, "move")
        n4.addConnection(n4, "suck")
        n4.addConnection(n8, "move")
        n5.addConnection(n1, "move")
        n5.addConnection(n7, "suck")
        n6.addConnection(n8, "suck")
        n6.addConnection(n2, "move")
        n7.addConnection(n3, "move")
        n7.addConnection(n7, "suck")
        n8.addConnection(n8, "suck")
        n8.addConnection(n4, "move")
        nodes = [n1, n2, n3, n4, n5, n6, n7, n8]
            # add nodes to graph
        for i in nodes:
            g.addNode(i)
        self.setGraph(g)
        

    def getGraph(self):
        return self.graph

    def setGraph(self, gr):
        if type(gr) == Graph:
            print('successfully initialized')
            self.graph = gr
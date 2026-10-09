from node import Node
class Graph:
    '''
    nodes: the list of nodes, these should be node objects
    '''
    nodes = []
    
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes
    
    def addEdge(self, sourceId, destId):
        pass

    def bfs(self, startId):
        start_node = 0
        for n in self.getNodes():              # grab node
            if n.getId() == startId:
                start_node = n

        if start_node == 0:                     # check for valid node
            return []
        path = [start_node]
        processed = []    # comprised of NodeIDS
        queue = [[start_node, [start_node]]]    # curr[0] is node curr[1] is path
        while queue != []:
            print("hello")
            skip = False
            curr = queue.pop(0)
            node = curr[0]               # node
            curr_path = curr[1]          # path leading up to node
            processed.append(node)
            print(node.getId())
            print(node.getTrash())
            print(node.getVac())
            print(f"path: {curr_path}")
            if node.getTrash() == [0,0]:            # if no trash end
                print("no trash")
                path = [curr_path.append(node)]    
                break
            for n in node.getConnections():
                skip = False
                print("looking for connections ...")
                print(f"curr: {n.getId()}")
                for i in processed:
                    if n.getId() == i.getId():
                        skip = True
                        print("skipped")
                if skip == False:
                    print("adding connection")
                    queue.append([n, curr_path.append(node)]) # none currpath left node fuckkk
        print("reached end")
        return path
        
    def dfs(self, startId):
        ##DEPTHFIRST SEARCH
        start_node = self.getNodes()[startId]
        path = [start_node]
        processed = []    # comprised of NodeIDS
        queue = [start_node]
        
        return path

    def __str__(self):
        pass
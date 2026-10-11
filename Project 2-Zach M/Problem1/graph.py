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

    """
        This function finds the goal using bfs
        Order of execution
        find node via for loop (later found to be uneccisary, since all nodes are already stored in ID order)
        initiate lists, for queue, process, and path
        initiate loop, using queue as stoping condition
            grab current node and path, also reseting variables used in the loop
            append node being searched to processed list
            if trash is [0,0]
                set path and break loop
            for each connection
                if connection has been searched, skip it
                otherwise add to queue
        
        ARGs: startId, id of first node
        RETURNS: List of Ids
    """
    def bfs(self, startId)->list:
        
        start_node = 0
        for n in self.getNodes():              # grab node
            
            if n.getId() == startId:
                start_node = n

        if start_node == 0:                     # check for valid node
            print("INVALID NODE")
            return []
        path = [start_node]
        processed = []    # comprised of NodeIDS
        queue = [[start_node, []]]    # curr[0] is node curr[1] is path
        while queue != []:
            skip = False
            curr = queue.pop(0)
            node = curr[0]               # node
            curr_path:list = curr[1]          # path leading up to node
            processed.append(node)
            if node.getTrash() == [0,0]:            # if no trash end
                path = curr_path + [node.getId()]   
                break
            for n in node.getConnections(): #check each connected node against nodes in processed
                skip = False
                for i in processed:
                    if n.getId() == i.getId():
                        skip = True
                if skip == False:   # if not already processed add to queue
                    print("adding connection")
                    queue.append([n, curr_path + [node.getId()]])
        
        return path
    """
        Function for searching nodes via dfs
        Order of execution:
            set found
            find current node
            if current nodes trash is gone
                return path, with true
            else
                for every connection...
                    if that connection has not been processed, recur to seach that connection. Set the value of the function call to
                    path, found 
                    if found == true
                        break out of loop
            return
        ARGS:
            node: id of node to search
            path: not for user, indicated path taken to current node
        RETURNS:
            Path taken to node
            found: indicates whether reccursion can end, or if no result was found
    """
    def dfs(self, node, path=[])->list:
    
        found = False
       
        ##DEPTHFIRST SEARCH
        curr_node = self.getNodes()[node-1]
        if curr_node.getTrash() == [0,0]:
            return path + [node], True
        else:
            
            for n in curr_node.getConnections():
                if n.getId() not in path and n.getId() != curr_node.getId():
                    path, found = self.dfs(n.getId(), path + [node])
                if found:
                    break
        return path, found

    def __str__(self):
        pass
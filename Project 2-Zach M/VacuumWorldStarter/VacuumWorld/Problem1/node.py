class Node:
    '''
    img: an image file (.png works) that shows the state
    id: the id for the state
    connections: a list of the other states that can be reached from this state
    what else do you want to add...?
    '''
    img = None
    id = -1
    connections = []
    #what else should you add?
    trash:list[int] = [] # 0=None, 1=Trash
    vac:str = "ERR" # Left or Right


    def __init__(self, img=None, nodeId=-1, trash=[], vac="ERR"):
        self.img = img
        self.id = nodeId
        self.trash = trash
        self.vac=vac
        self.connections = []

    def getTrash(self):
        return self.trash
        
    def getImg(self):
        return self.img

    def getVac(self):
        return self.vac
    def getId(self):
        return self.id

    def getConnections(self):
        return self.connections
    
    def setImg(self, img):
        self.img = img

    def setId(self, nodeId):
        self.id = nodeId

    def addConnection(self, otherNode, action):
        self.connections.append(otherNode)
        pass

    def __str__(self):
        pass
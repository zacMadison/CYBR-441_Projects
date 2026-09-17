import student
import node

class Deque:
    # Each index of node will contain two values, the first being the student and the next being the next node
    
    _len:int = 0
    _front = None
    _back = None

    def __init__(self):
        pass

    # helpers
    def incrementLen(self):
         self.setLen(self.getLen + 1)

    def deincrementLen(self):
         self.setLen(self.getLen - 1)

    """
    This function sets the front node to new node with a new student
    if there is no front node it is created
    if there is a front node a new front is created with a point to the old front
        , then the new front is set as the front
    len is incremented

    Args: new_student: variable created from the student class
    """
    def addFront(self, new_student:student):
            if self.getLen == 0:
                new_node = node(student)
                self.setFront(new_node)
                self.setBack(new_node)
            else:
                old_front:node = self.getFront()
                new_front:node = node(new_student, old_front)
                self.setFront(new_front)
            self.incrementLen()

    """
    This function sets the back node to new node with a new student
    if there are no nodes a new one is created
    otherwise the current back node is set to point to the new node, and the new node is set to be the back node
    len is incremented

    Args: new_student: variable created from the student class
    """
    def addBack(self, new_student:student):
        if self.getLen == 0:
            new_node = node(student)
            self.setFront(new_node)
            self.setBack(new_node)
        else:
            back_node:node = self.getBack()
            new_node:node = node(new_student)
            back_node.setNext(new_node)
            self.setBack(new_node)
            self.incrementLen()

    """
    This function removes the front item by changing the front node to the next node
    Before the current front is removed the value is printed, which should print the __str__ func in student
    """
    def popFront(self):
         print(self.getFront().getValue())
         self.setFront(self.getFront().getNext())

    """
    This function removes the back node by reassigning the back the node pointing to the back node
    if the back and front are the same then they are both set to None
    Len is deincremented
    """
    def popBack(self):
        print(self.getBack().getValue())
        if self.getFront() == self.getBack():
             self.setFront(None)
             self.setBack(None)
        else:
            target_node:node = self.getBack()
            curr_node:node =  self.getFront()
            while curr_node.getNext() != target_node:
                 curr_node:node = curr_node.getNext()
            curr_node.setNext(None)
            self.setBack(curr_node)
        self.deincrementLen()

                 
        

    # Getters
    def getFront(self)->node:
         return self._front

    def getBack(self)->node:
         return self._back

    def getLen(self)->int:
         return self._len
    # Setters
    def setFront(self, front:node):
        self._front = front
    
    def setBack(self, back:node):
        self._back = back
    
    def setLen(self, len:int):
        self._len = len


    
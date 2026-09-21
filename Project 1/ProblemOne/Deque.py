import Student as stu
import Node as Node

class Deque:
    # Each index of Node will contain two values, the first being the Student and the next being the next Node
    
    _len:int = 0
    _front = None
    _back = None

    def __init__(self):
        pass

    # helpers
    def incrementLen(self):
         self.setLen(self.getLen() + 1)

    def deincrementLen(self):
         self.setLen(self.getLen() - 1)

    """
    This function sets the front Node to new Node with a new Student
    if there is no front Node it is created
    if there is a front Node a new front is created with a point to the old front
        , then the new front is set as the front
    len is incremented

    Args: new_Student: variable created from the Student class
    """
    def addFront(self, new_Student:stu.Student):
            if self.getLen() == 0:
                new_node = Node.Node(new_Student)
                self.setFront(new_node)
                self.setBack(new_node)
                self.incrementLen()
            else:
                old_front:Node.Node = self.getFront()
                new_front:Node.Node = Node.Node(new_Student, old_front)
                self.setFront(new_front)
            self.incrementLen()

    """
    This function sets the back Node to new Node with a new Student
    if there are no Nodes a new one is created
    otherwise the current back Node is set to point to the new Node, and the new Node is set to be the back Node
    len is incremented

    Args: new_Student: variable created from the Student class
    """
    def addBack(self, new_Student:stu.Student):
        if self.getLen() == 0:
            new_node = Node.Node(new_Student)
            self.setFront(new_node)
            self.setBack(new_node)
            self.incrementLen()
        else:
            back_node:Node.Node = self.getBack()
            new_node:Node.Node = Node.Node(new_Student)
            back_node.setNext(new_node)
            self.setBack(new_node)
            self.incrementLen()

    """
    This function removes the front item by changing the front Node to the next Node
    Before the current front is removed the value is printed, which should print the __str__ func in Student
    """
    def removeFront(self):
         
        self.setFront(self.getFront().getNext())

    """
    This function removes the back Node by reassigning the back the Node pointing to the back Node
    if the back and front are the same then they are both set to None
    Len is deincremented
    """
    def removeBack(self):
        if self.getFront() == self.getBack():
             self.setFront(None)
             self.setBack(None)
        else:
            target_node:Node.Node = self.getBack()
            curr_node:Node.Node =  self.getFront()
            while curr_node.getNext() != target_node:
                 curr_node:Node.Node = curr_node.getNext()
            curr_node.setNext(None)
            self.setBack(curr_node)
        self.deincrementLen()


    """
    This function starts at the beginning of the linked list by getting the front Node, the function will then check if the first Node matches the target name, if it does found is set equal to true
    and returns
    if the first Node does not match, then the entire linked list will be iterated through, also setting found equal to true if a match is found, found is return after this iteration, 
    indicating whether or not the Student exists in the linked list. If found is found while iterating the loop is exited early
    Args: 
        name
            Accepts a String Value that represents the name of a Student
    Returned Values:
        found
            A boolean variable that indicates whether or not the input name matches any Student in the linked list
    """
    def search(self, name:str)->bool:
        curr_node:Node.Node = self.getFront()
        found:bool = False
        if curr_node.getValue().getName() == name:
            found = True
        else:
            while curr_node.getNext() != None and found == False:
                if curr_node.getNext().getValue().getName() == name:
                    found = True
                curr_node:Node.Node = curr_node.getNext()
        return found

    """
    This function starts at the beginning of the linked list by getting the front Node, the function will then check if the first Node matches the target name, if it does found is set equal to true
    and returns. Additionally self.removeFront is called because we know that the target is at the front

    if the first Node does not match, then the entire linked list will be iterated through, the target Node is checked for by searching one Node ahead of the current Node. 
    If the target Node is found it is removed by setting the the next Node the the Node in front of the target Node. Found is set equal to true after this
    Args: 
        name
            Accepts a String Value that represents the name of a Student
    Returned Values:
        found
            A boolean variable that indicates whether or not the input name matches any Student in the linked list
    """
    def remove(self, name:str)->bool:
        curr_node:Node.Node = self.getFront()
        found:bool = False
        if curr_node.getValue().getName() == name:
            found = True
            self.removeFront()
            self.deincrementLen()
        else:
            while found ==False and curr_node.getNext() != None:
                if curr_node.getNext().getValue().getName() == name:
                    found = True
                    curr_node.setNext(curr_node.getNext().getNext())
                    self.deincrementLen()
                curr_node:Node.Node = curr_node.getNext()
        return found

    # Getters
    def getFront(self)->Node.Node:
         return self._front

    def getBack(self)->Node.Node:
         return self._back

    def getLen(self)->int:
         return self._len
    # Setters
    def setFront(self, front:Node.Node):
        self._front = front
    
    def setBack(self, back:Node.Node):
        self._back = back
    
    def setLen(self, len:int):
        self._len = len

    # This function prints all Student, primarily for potential troubleshooting
    def printQueue(self):
        if self.getFront() == None:
            print(f"NO EXISTING STUDENTS")
        else:
            print("STUDENTS\n______________________________")
            curr_node = self.getFront()
            while curr_node != None:
                # This Prints Student class, which has a __str__ function
                print(curr_node.getValue())
                curr_node = curr_node.getNext()
            print("___________________________\nEND")
    
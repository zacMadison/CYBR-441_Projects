import Node as node


class BinarySearchTree:
    _root:node.Node = None

    

    # helpers

    """
    compares a new value to the existing value in the BST, starting at the root.
    if the vlaue is lower than the node currently being processed, then we look at the left child.
    otherwise we will look at the right child.
    if either of these are empty, we will place the new node there and end the loop, otherwise we set the currently processing node to that child and continue

    args:
        new_value(int): An integer that represents a new value to be added to the bst
    """
    def insertion(self, new_value:int):
        running = True
        new_node = node.Node(new_value, None, None)

        # if the root is empty all we need to do is set it
        if self.getRoot() == None:
            self.setRoot(new_node)
        else:
            curr_node = self.getRoot()
            # if empty node is found where we are looking loop ends and value is set there
            while running:
                # if new value is lower than current node look left
                if new_node.getPayload() <= curr_node.getPayload():
                    if curr_node.getChildLeft() == None:
                        curr_node.setChildLeft(new_node)
                        running = False
                    else:
                        curr_node = curr_node.getChildLeft()
                # otherwise look right
                elif new_node.getPayload() > curr_node.getPayload():
                    if curr_node.getChildRight() == None:
                        curr_node.setChildRight(new_node)
                        running = False
                    else:
                        curr_node = curr_node.getChildRight()
        
    # IMPORTANT : PLACE DELETION CBT FUNCTION HERE new value must be leaf

    """
    Dev Note:) this function is a mess and probably would have been easier recursively:))))
    also I'm not entirely sure del has any function some troubleshooting seemed to indicate that it is not

    This function takes a target int and searches the BST by comparing to value of current 
    when the value is found the current node is replace by the pointer of its parent node to be reset to a valid node under the current node
    the current nodes children from the side of the tree oposite of the replacement are given to the replacement
     after this del current node is called to remove any potentially forgotten references to this node

     if the current node is the root 
     ARGS: target value: represents value of target node
     returns: bool representing success or failure
    """
    def deletion(self, target:int)->bool:
        
        found = False
        running = True
        curr_node = self.getRoot()
        prev_node = None
        direction:str = None
        if curr_node.getPayload() == target:
            found = True
            print("root")

        while running and not found:
            print("Searching...")
            if curr_node.getPayload() == target:
                found = True
            else:
                prev_node = curr_node
                if curr_node.getChildRight() == None and curr_node.getChildLeft() == None:
                    running = False
                elif target >curr_node.getPayload():
                    curr_node = curr_node.getChildRight()
                    direction = "right"
                elif target < curr_node.getPayload():
                    curr_node = curr_node.getChildLeft()
                    direction = "left"
                

        if found == True and running == True:
            print("looking for valid child")
            print(curr_node.getChildRight())
            # if there are no children
            if curr_node.getChildLeft() == None and curr_node.getChildRight() == None:
                self.replace(new=None, prev=prev_node, direction=direction)
                del curr_node
            # if there is one child
            elif curr_node.getChildRight() == None:
                self.replace(new=curr_node.getChildLeft(), prev=prev_node, direction=direction)
                del curr_node
            elif curr_node.getChildLeft() == None:
                self.replace(new=curr_node.getChildRight(), prev=prev_node, direction=direction)
                del cur
            # if there are two children
            else:
                new_node:node.Node = curr_node.getChildLeft()
                while running == True:
                    if new_node.getChildRight() == None:
                        running = False
                        new_node.setChildRight(curr_node.getChildRight())
                        self.replace(new=new_node, prev=prev_node, direction=direction)
                        del curr_node
                    else:
                        new_node = new_node.getChildRight()
                
        # PLACE ACTUAL PART WHERE WE REPLACE HERE
        return found

    """
        This function replaces nodes using information from deletion function
        args:
            new- new node that is replacing an old node
            prev- previous node whose corresponding pointer will be overwritten to a new node
            direction- indicates which child needs to be overwritten on prev
    """
    def replace(self, new:node.Node, prev:node.Node, direction):
        if prev == None:
            self.setRoot(new)
        elif direction == "left":
            prev.setChildLeft(new)
        else:
            prev.setChildRight(new)


            
        
        

    """
    This function iterates through the BST searching for a target value, if this value is lower or higher than current node, the corresponding child is searched
    if an empty node is reached, looping is terminated. result is returned at end of function. if the target is the root, then looping is skiped

    args:
        target(int): represents value to search for
    returned values: 
        target(bool): indicates whether or not the value being searched for was found
    """
    def search(self, target:int)->bool:
        found = False
        curr_node:node.Node = self.getRoot()
        if target == curr_node:
            found = True
        else:
            running = True
            while not found and running:
                if target == curr_node.getPayload():
                    found = True
                elif target < curr_node.getPayload():
                    curr_node = curr_node.getChildLeft()
                elif target>curr_node.getPayload():
                    curr_node = curr_node.getChildRight()
                if curr_node == None:
                    running = False
        return found

    # traversal

    """
    This function performs an inorder search recursivly
    because inorder is *shocker*; In order, we recurse over left child, append ourself, then recurse of right
    Args:
    curr_node: only for recursion
    """    
    def inorder(self, curr_node:node.Node=None)->list:
        nodes:list = []
        if curr_node== None:
            curr_node = self.getRoot()

        if curr_node.getChildLeft() != None:
            nodes.extend(self.inorder(curr_node.getChildLeft()))
        nodes.append(curr_node.getPayload())
        if curr_node.getChildRight() != None:
            nodes.extend(self.inorder(curr_node.getChildRight()))
        return nodes

    """
    identical to inorder, except we append current node before recursing
    """
    def preorder(self, curr_node:node.Node=None)->list:
        nodes:list = []
        if curr_node == None:
            curr_node = self.getRoot()
        
        nodes.append(curr_node.getPayload())
        if curr_node.getChildLeft() != None:
            nodes.extend(self.preorder(curr_node.getChildLeft()))
        if curr_node.getChildRight() != None:
            nodes.extend(self.preorder(curr_node.getChildRight()))

        return nodes

    def postorder(self, curr_node:node.Node=None)->list:
        nodes:list = []
        if curr_node == None:
            curr_node = self.getRoot()
        
        if curr_node.getChildLeft() != None:
            nodes.extend(self.postorder(curr_node.getChildLeft()))
        if curr_node.getChildRight() != None:
            nodes.extend(self.postorder(curr_node.getChildRight()))
        nodes.append(curr_node.getPayload())

        return nodes


    # getters
    def getRoot(self)->node.Node:
        return self._root

    # setters
    def setRoot(self, root:node.Node):
        self._root = root


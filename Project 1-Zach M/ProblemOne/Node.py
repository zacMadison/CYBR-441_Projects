# this is a class that stores a value and a pointer for implemenmtation in a linked list.

# allows parameter referencing own class to be defined
from typing import Self


class Node:
    _value = None
    _next = None
    def __init__(self, value = None, next:Self = None):
        # value type will remain undefined, because this is a generic node
        self.setValue(value)
        self.setNext(next)
    

    # Getters
    
    def getValue(self):
        return self._value

    def getNext(self)->Self:
        return self._next
    # Setters
    def setValue(self, value):
        self._value = value

    def setNext(self, next:Self):
        self._next = next

    
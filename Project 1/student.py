# This class stores info about students and will function operate as the node for a queue
class Student:
    _name:str = "NULL"
    _age:int = -1
    _gpa:float = -1

    def __init__(self, name:str = "NULL", age:int = -1, gpa:float = -1):
        self.setName = name
        self.setAge  = age
        self.setGPA = gpa

    # helpers (none for this class)

    # getters
    def getName(self)->str:
        return self._name

    def getAge(self)->int:
        return self._age

    def getGPA(self)->float:
        return self._gpa
    
    # setters
    def setName(self, new_name:str):
        self._name = new_name

    def setAge(self, new_age:int):
        self._age = new_age

    def setGPA(self, new_GPA:float):
        self._gpa = new_GPA

    # if class is printed print all stored variables
    def __str__(self):
        pass
import Deque as LinkedList
import Student as stu
"""
    LinkedList functions
        addFront
        addBack
        removeFront
        removeBack
        search
        remove
"""
"""
    Student init
        name
        age
        gpa
"""
# Test one: Add front on empty list: WORKS
# Test two: Add back on empty list: WORKS
# test three: add front and back on non empty list: WORKS
# teest Four: remove from front and back: WORKS
# test Five: use search and remove: WORKS
def main():
    
    s1 = stu.Student(f"Zach", 21, 3.0)
    s2 = stu.Student(f"Raly", 1, 20)
    
    s3 = stu.Student(f"?????", 999, 3.4)
    s4 = stu.Student(f"last(name)", 30, 1.0)
    lst = LinkedList.Deque()
    
    lst.addBack(s1)
    lst.addFront(s2)
    lst.addFront(s3)
    lst.addBack(s4)

    lst.printQueue()
    pass


if __name__ == "__main__":
    main()
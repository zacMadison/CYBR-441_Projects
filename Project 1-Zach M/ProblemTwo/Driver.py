import BST as bst

"""bst functions
    insertion WORKING
    deletion WORKING
    search WORKING
    inorder WORKING
    preorder WORKING
    postorder WORKING
"""
def main():
    tree = bst.BinarySearchTree()
    print("hello")
    tree.insertion(5)
    tree.insertion(1)
    tree.insertion(7)
    tree.insertion(2)
    tree.insertion(9)

    """
    result = tree.deletion(5)
    print(result)
    print(tree.search(5))
    """
    #inorder
    print(tree.inorder())
    print(tree.preorder())
    print(tree.postorder())
    pass

if __name__ == "__main__":
    main()
class Node:
    def __init__(self,value):
        self.value = value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def _r_insert(self,current_node,value):
        if current_node==None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self._r_insert(current_node.left,value)
        if value > current_node.value:
            current_node.right = self._r_insert(current_node.right,value)
        return current_node

    def r_insert(self,value):
        if self.root is None:
            self.root = Node(value)
        return self._r_insert(self.root,value)
myTree=BinarySearchTree()
myTree.r_insert(2)
myTree.r_insert(1)
myTree.r_insert(3)
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
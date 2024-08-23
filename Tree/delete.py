class Node:
    def __init__(self,value):
        self.value = value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if self.root==None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if new_node.value==temp.value:
                return False
            elif new_node.value<temp.value:
                if temp.left==None:
                    temp.left=new_node
                    return True
                else:
                    temp=temp.left
            else:
                if temp.right==None:
                    temp.right=new_node
                    return True
                else:
                    temp=temp.right

    def min_value(self,current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def _delete(self,value):
        self.__delete(self.root, value)
    
    def __delete(self,current_node,value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete(current_node.right, value)
        else:
            if current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            elif current_node.left is None and current_node.right is None:
                return None
            else:
                min_node = self.min_value(current_node.right)
                current_node.value = min_node
                current_node.right = self.__delete(current_node.right,value)
        return current_node



myTree=BinarySearchTree()
myTree.insert(2)
myTree.insert(1)
myTree.insert(3)
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
print("After deleting")
myTree._delete(2)
print(myTree.root.value)
print(myTree.root.left.value)

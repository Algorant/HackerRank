'''
Traverse a binary tree in "in-order traversal" mode. That is:
left to right and top to bottom.
'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = [root] if root else [] #where to begin (aka pointer)

        while queue:
            node = queue.pop() #take out the value
            print(node.data, end=" ") #print it

            if node.left: queue.insert(0, node.left)
            if node.right: queue.insert(0, node.right)

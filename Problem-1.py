"""
# Problem 1
Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)


"""
from collections import deque
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

#BFS Time - O(N), SPACE- O(N/2)
def Levelorder_BFS(root: TreeNode):
    if root == None:
        return None
    result=[]
    q = deque()
    q.append(root)
    while q.count()!=0:
        size= len(q)
        temp=[]
        for i in range(size):  # loop for the children of current node
            node=q.popleft()
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(temp)
    return result




#DFS Time - O(N), SPACE- O(max(DEPTH)
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode):
        self.stack=[]
        if root==None:
            return
        self.dfs(root, 0)
        return self.stack

    def dfs(self, root,level):
        if root==None:
            return
        if len(self.stack)==level:  #if length of stack == level then add empty list in stack
            self.stack.append([])
        self.stack[level].append(root.val)    #append root in stack at postion equal to level number

        self.dfs(root.left,level+1)
        self.dfs(root.right,level+1)




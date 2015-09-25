# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
##### method 1 iterative: 52ms
    
    def levelOrderBottom(self, root):
        if not root: return []; 
        curr = []
        res = []
        curr.append(root)
        while root and curr: 
            size = len(curr)
            currLevel = []
            for i in range(size):
                root = curr.pop(0)
                currLevel.append(root.val)
                if root.left:  curr.append(root.left)
                if root.right: curr.append(root.right)
            res.insert(0, currLevel ) 
        return res
        
##### method 2 recursive: 60 ms
    def preorder(self, root, level, res ):

        if root : 
            if len(res) < level + 1: res.append([])
            res[level].append(root.val) 
            self.preorder( root.left, level + 1, res ) 
            self.preorder( root.right, level + 1, res ) 
            
    def levelOrderBottom_recursive(self, root):
        res = []
        self.preorder( root, 0, res) 
        return res[::-1]
        

            
        


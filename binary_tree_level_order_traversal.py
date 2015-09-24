# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # def bfs( root, queue, out ): 
        if root == None: return []
        if root.left == None and root.right == None: return [[root.val]] 
        queue = [root]; out = [];  
        while queue: 
            level = [];
            size = len(queue) 
            for i in range( size ) :
                root = queue.pop(0)
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            out.append(level)
        return out

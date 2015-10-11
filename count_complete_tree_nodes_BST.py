# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ### 2^h 
        def isLeft( p, h) :
            for _ in range(h):
                p = p.left
            return p 
        
        if not root: return 0 
        h, curr = 0, root
        while curr.left: h += 1; curr = curr.left
        
        ### binary search on the tree
        curr, cnt = root, 1 
        while h:
            if isLeft( curr.right, h-1): 
                curr, cnt = curr.right, cnt * 2 + 1
            else:
                curr, cnt = curr.left, cnt * 2
            h -= 1
        return cnt
        
        ### TLE, not using the fact that it's complete BT
        # if not root: return 0
        # else:
        #     return 1 + self.countNodes( root.left) + self.countNodes(root.right)
            
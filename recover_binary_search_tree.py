# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1, self.n2, self.prev  = None, None, None

        def dfs(root):
            if root:
                dfs(root.left) 
                if self.prev and self.prev.val > root.val:
                    self.n2 = root
                    if self.n1 == None: 
                        self.n1 = self.prev
                self.prev = root 
                dfs(root.right) 
        dfs(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        
        ### -------- O(n) space methods
        # def dfs_inorder(root, lists, plists):
        #     if root:
        #         dfs_inorder(root.left, lists, plists)
        #         lists.append(root.val); plists.append(root)
        #         dfs_inorder(root.right, lists, plists)
        # lists = [] ; plists = []
        # dfs_inorder(root, lists, plists)
        # lists.sort()
        # for i in range(len(plists)):
        #     plists[i].val = lists[i] 
            
                
        

            
            
                
        
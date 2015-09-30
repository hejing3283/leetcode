# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bsf(self, idxL, idxR ):
        if idxL > idxR : return None
	mid = (idxL + idxR )
        mid = (mid-1)/2 if mid%2 else mid/2
        root = TreeNode( self.nums[  mid  ] ) 
        print root.val, idxL, idxR
        root.left = self.bsf( idxL,  mid - 1  ) #### mid -1 is the idxR
        root.right = self.bsf( mid + 1, idxR  ) 
            
        return root 
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        return self.bsf(0, len(nums)-1 )
        

        

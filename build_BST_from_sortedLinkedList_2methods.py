# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

#### Method 1 : 
    # def dfs( self, idxL, idxR):
    #     if idxL > idxR : return None
    #     mid =  idxL + idxR 
    #     mid =  (mid-1)/ 2 if mid%2 else mid/2
    #     root = TreeNode( self.array[mid] )
    #     root.left = self.dfs( idxL, mid-1 ) 
    #     root.right = self.dfs (  mid+1, idxR)
    #     return  root
    # def sortedListToBST(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: TreeNode
    #     """
    #     ## the lenght 
    #     if not head: return []
    #     self.array = [] 
    #     while head : 
    #         self.array.append( head.val)
    #         head = head.next
    #     return self.dfs( 0, len( self.array) - 1 )

 #### Method 2 :       
    def sortedListToBST(self, head):
        count = 0 ; p = head 
        while p:
            count += 1
            p = p.next
        
        def dfs_2 ( head, count, nextNode) :
            if count == 0:
                nextNode.next = head
                return None
            leftTree = dfs_2( head, count / 2, nextNode) 
            root = TreeNode( nextNode.next.val) 
            nextNode.next = nextNode.next.next # one step right 
            rightTree = dfs_2( nextNode.next, count - 1 - count/2, nextNode) 
            root.left = leftTree
            root.right = rightTree
            return root
        return dfs_2( head, count, TreeNode(0))
            
                
                

            
        
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0: return head
        if head == None : return head 
        
        # count ele
        cnt = 0
        dummy = ListNode(0) 
        dummy.next = head 
        p = dummy
        while p.next:
            p = p.next; cnt +=1 
        step = cnt - ( k % cnt ) 
        p.next = dummy.next
        for i in range(step):
            p = p.next 
        head = p.next 
        p.next = None 
        
        return head 
        
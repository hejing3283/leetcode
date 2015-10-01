# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        ## O(n) time and O(n) space
        """
        if not head : return
        
        dummy = RandomListNode(0) 
        p = dummy; q = head;  myMap = {}
        while q:
            p.next = RandomListNode(q.label)
            myMap[q] = p.next
            q = q.next; 
            p = p.next
            
        p = dummy; q = head
        while q:
            if q.random: 
                p.next.random = myMap[q.random]
            p = p.next
            q = q.next
        
        return dummy.next
        
        ### ---- methods 2: o(n) time and o(1) space
        
        
            
            
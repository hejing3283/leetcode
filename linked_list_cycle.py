# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ### O(1) space
        fastP = slowP = head
        while fastP != None and fastP.next != None:
            fastP = fastP.next.next
            slowP = slowP.next
            if fastP == slowP : return True
        return False 
        
        ### AC O(n) space
        # dummy = ListNode(0)
        # dummy.next = head
        # visited = set([])
        # p = dummy.next
        # while p:
        #     if p not in visited : visited.add(p) 
        #     else: return True
        #     p = p.next
        # return False 
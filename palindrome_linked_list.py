# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ### still change to array and do it
        ### reverse the list and compare
        if not head: return True
        
        slow = fast = head
        ### fast.next cannot be None
        while fast.next and fast.next.next: 
            slow = slow.next
            fast = fast.next.next
        
        p, last = slow.next, None
        while p: 
            pnext = p.next
            p.next = last
            last, p = p, pnext
          
        p1  = last; p2 = head
        while p1 and p1.val == p2.val:
            p1 = p1.next; p2 = p2.next
        
        ### resume the order
        # p, last = last, None
        # while p : 
        #     pnext = p.next
        #     p.next = last
        #     last, p = p, pnext
        # slow.next = last
        
        return p1 is None
        
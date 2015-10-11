# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None: return
        
        dummy = ListNode(0); dummy.next = head
        p = dummy.next; n = 0 
        while p:    p = p.next ;  n += 1
        if n == 1: return
        stack = []
        p = dummy.next ; i = 0
        while p: 
            if i >= n/2: stack.append( p ) 
            p = p.next ; i += 1
        p = dummy.next
        while stack:
            tmp = p.next
            p.next = stack.pop()
            p.next.next = tmp
            p = p.next.next
        p.next = None
        head = dummy.next
        
            
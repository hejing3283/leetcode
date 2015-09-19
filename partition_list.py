# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None : return head
        tmp = head
        h1 = ListNode(0); h2 = ListNode(0)
        p1 = h1;  p2 = h2
        while tmp:
            if tmp.val < x:
                p1.next = tmp
                tmp = tmp.next
                p1 = p1.next
                p1.next = None
            else:
                p2.next = tmp
                tmp = tmp.next 
                p2 = p2.next
                p2.next = None
        p1.next = h2.next
        head = h1.next
        return head
                
        
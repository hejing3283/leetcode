# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head : return head
        if not head.next : return (head if head.val != val else None)
        dummy = ListNode(0); dummy.next = head 
        p = dummy
        while p.next:
            # print p.val, p.next.val
            if p.next.val == val:
                p.next = p.next.next if p.next.next else None
            else:
                p = p.next
        p.next = None
        return dummy.next
        
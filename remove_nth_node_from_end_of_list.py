# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ##### learned from online AC
        dummy = ListNode(0); dummy.next = head
        fast = slow = dummy
        for _ in xrange(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        ##### Not working for boundary cases
        # if not head.next and n == 1: return []
        # if not head : return []
        # count = 1
        # dummy = ListNode(0) ; dummy.next = head 
        # slow = head; fast = head.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     count += 1
        # if fast != None:  n -=1 
        # if count > n :
        #     count = count - n 
        #     head = slow
        # else : 
        #     count = count * 2 - n 
        # i = 1
        # while i < count:
        #     head = head.next
        #     i += 1
        # head.next = head.next.next
        # return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cnt = 0 
        p1 = l1; p2 = l2; 
        dummy = ListNode(0) 
        p = dummy
        carry = 0 ;
        while p1 or p2 :
            if p1 and p2:
                p.next = ListNode( (p1.val + p2.val + carry) % 10)
                carry = (p1.val + p2.val + carry) / 10 
                p1 = p1.next; p2 = p2.next
            elif p1 and not p2: 
                p.next = ListNode( (p1.val + carry) % 10)
                carry = (p1.val + carry) / 10
                p1 = p1.next
            else:
                p.next = ListNode( (p2.val + carry) % 10)
                carry = (p2.val + carry) / 10
                p2 = p2.next
            p = p.next
        if carry :  p.next = ListNode(carry)  
        return dummy.next
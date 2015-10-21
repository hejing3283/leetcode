# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = 0, 0 
        pA, pB = headA, headB
        while pA : 
            lenA += 1; pA = pA.next
        while pB :
            lenB += 1; pB = pB.next
            
        pA, pB = headA, headB
        if lenA > lenB : 
            dist = lenA - lenB;
            for i in range(dist) : 
                pA = pA.next    
        if lenB > lenA : 
            dist = lenB - lenA; 
            for i in range(dist):
                pB = pB.next
            
        while pA and pB:
            if pA.val == pB.val: 
                return pA
            else:
                pA, pB = pA.next, pB.next
        return None
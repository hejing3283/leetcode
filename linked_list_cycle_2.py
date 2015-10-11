# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ## O(n) space solution is trivial 
        
        ## O(1) space solution need some thought
        ### onlie solution 
        dummy = ListNode(0); dummy.next = head
        
        pslow = pfast = dummy.next; meet = None;
        while pfast != None and pfast.next != None:
            pfast = pfast.next.next
            pslow = pslow.next
            if pfast == pslow: 
                meet = pslow;
                break
        if meet == None : return
        
        pfast = dummy.next
        while pfast != pslow :
            pfast = pfast.next
            pslow = pslow.next
        return pfast
        
        # ## brute fore to try every node before meet.... O(kn) time complexity , TLE

        # dummy = ListNode(0); dummy.next = head
        
        # pslow = pfast = dummy.next; meet = None
        # while pfast != None and pfast.next != None:
        #     pfast = pfast.next.next
        #     pslow = pslow.next
        #     if pfast == pslow: 
        #         meet = pslow;
        #         break
        # if meet == None : return
        # dummy = ListNode(0); dummy.next = meet
        # p = dummy.next
        # while head :
        #     if head == p: return head
        #     while True :
        #         if head == p: return head
        #         p = p.next
        #         if p == meet:  p = dummy.next; break
        #     head = head.next
        # return 

        
        
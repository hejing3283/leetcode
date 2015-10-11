# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ### 2 pointer and merge sort
        if not head or not head.next :
            return head
        slow = head; 
        fast = head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        rlist = self.sortList(slow.next)
        slow.next = None
        llist = self.sortList(head)
        return self.mergeList( llist, rlist) 
        
        
    def mergeList( self, l, r) :
        nHead = ListNode(0)
        prev = nHead
        while l and r :
            if l.val < r.val:
                prev.next = l 
                l = l.next 
            else: 
                ## exchange
                prev.next = r
                r = r.next 
            prev = prev.next 
        prev.next = l or r  ### left and right, at least one is None
        return nHead.next
        
        ### kind of cheating 
        # if head == None: return None
        # dummy = ListNode(0)
        # dummy.next = head
        # p = dummy.next
        # array = []
        # while p:
        #   array.append(p.val)
        #   p = p.next
        
        # array.sort()
        # p = dummy.next 
        # while p:
        #     p.val = array.pop(0)
        #     p = p.next
        # return dummy.next 
        
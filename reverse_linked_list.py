# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # prev = None
        # curr = head
        # while curr:
        #     nextNode = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextNode
        prev, curr = None, head
        while curr:
            curr.next, prev, curr  = prev, curr, curr.next
        return prev
        
        
        ### convert to array
        # array = [] 
        # p = head
        # while p:
        #     array.append(p.val)
        #     p = p.next
        
        # p = head
        # while p:
        #     p.val = array.pop()
        #     p = p.next 
        # return head 
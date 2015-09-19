# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n : return head 
        if head == None or head.next == None : return head
        if m > n : m , n = n , m 
        dummy = ListNode(0); dummy.next = head 
        head1 = dummy
        for i in range( m -1 ) :
            head1 = head1.next 
        p = head1.next 
        for i in range( n - m ) : 
            ## reveser each pair
            tmp  = head1.next
            head1.next = p.next 
            p.next = p.next.next
            head1.next.next = tmp 
        return dummy.next 
                    
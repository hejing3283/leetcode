# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        ## O(n) time and O(n) space
        """
	if not head : return
        dummy = RandomListNode(0) 
        p = dummy; q = head;  map = {}

        while q:
            p.next = RandomListNode(q.label)
            map[ id(q) ] = p.next
            q = q.next; 
            p = p.next

        p = dummy; q = head
        while q :
	    if q.random: 
	      p.next.random = map[ id(q.random) ]
	    p = p.next
	    q = q.next
        
        return dummy.next
        
        ### ---- methods 2: o(n) time and o(1) space
sol = Solution()
head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.next = RandomListNode(3)
head.random = head.next
head.next.random = head
head.next.next.random = head.next.next

head = RandomListNode(-1)
head.next = RandomListNode(1)
head.random = head 
head.next.random = head.next
newHeads = sol.copyRandomList(head)
while head != None:
    print head.label, " ", (head.random.val if not head.random else None)
    head = head.next
print "---------"
while newHeads != None:
    print newHeads.label, " ", (newHeads.random.val if not newHeads.random else None)
    newHeads = newHeads.next



        
        
            
            

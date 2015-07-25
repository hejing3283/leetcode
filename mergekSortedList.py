class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
  import heapq
  if not lists :
    return None
  heap = []
  for node in lists:
    if node:
      heap.append((node.val,node))
  heapq.heapify(heap) 
  head = ListNode(0); curr = head 
  while heap:
    pop = heapq.heappop(heap)
    curr.next = ListNode(pop[0])
    curr = curr.next
    if pop[1].next:
      heapq.heappush(heap, (pop[1].next.val, pop[1].next))
  return head.next

l1 = ListNode(-1)
l1.next = ListNode(1)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(7)

temp = ListNode(9)
l2 = ListNode(8); l2.next = temp
temp =ListNode(0); temp.next = l2
l2 = temp

temp = ListNode(15)
l3 = ListNode(11); l3.next = temp
temp =ListNode(-3); temp.next = l3
l3 = temp

out = mergeKLists( [l2, l1, l3] )
p = out 
while p:
  print p.val,
  p = p.next

out = mergeKLists( [[]] )
out = mergeKLists( [ListNode(-1),ListNode(-6),ListNode(1)] )
p = out 
while p:
  print p.val,
  p = p.next

 

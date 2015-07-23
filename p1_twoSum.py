#!/usr/bin/python
#J.HE
#Desp.:
def partition(A, left, right):
  '''
  split arrray according to it's median
  '''
  pL = left
  pR = right
  pivot = A[left]
  while pL < pR :
    while A[pL] > pivot and pL < right :
      pL += 1
    while A[pR] < pivot and pR > left:
      pR -= 1
    if pL < pR:
      temp = A[pL]; A[pL] = A[pR]; A[pR] = temp 
  mid = pR 
  temp = A[left]; A[left] =A[mid]; A[mid] = temp 
  return A

def twoSum( a, t ):
  ## return indices of the 2 numbers, idx1 < idx2, not 0-based
  ## input array of integers, target number
  lenA = len(a)

  a = partition(a, 0, lenA - 1)
  len1 = lenA/2 ; len2 = lenA - len1
  alo = a[:len1]
  aup = a[len1:]
  for t1 in alo:
    t2 = t - t1
    aup = partition(aup, 0, len2 - 1)
    if aup[
    
  return 
if __name__ == '__main__':
  A = [2,7,1,11,15]
  print A, partition(A, 0, len(A)-1  )
  # print( twoSum([2,7,11,15], 9 ) )
  # print( twoSum([2,7,11,15], 17 ) )

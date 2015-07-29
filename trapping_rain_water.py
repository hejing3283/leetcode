def trap(A):
  # @param {integer[]} A
  # @return {integer}
  if len(A) < 2: return 0
  pL = 0; pR = len(A) - 1 
  water = 0; 
  while pL < pR :
    while pL < pR and A[pL] == 0: pL += 1
    while pL < pR and A[pR] == 0: pR -= 1
    minH = min(A[pL], A[pR])
    curr = 0 
    for i in range(pL, pR+1):
      if A[i] > minH:
	A[i] -= minH 
      else:
	curr += minH - A[i] 
	A[i] = 0 
    water += curr 

  return  water

A = [0,1,0,2,1,0,1,3,2,1,2,1] 
wa = trap(A); print wa, wa == 6
# print trap([]) == 0
# print trap([1]) == 0
# print trap([1,1]) ==  0
# print trap([1,1,0]) == 0
# print trap([1,2,3,4]) == 0
# print trap([1,2,3,4,0,1]) == 1

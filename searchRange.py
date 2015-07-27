def searchRange(nums, t):
  n = len(nums)
  if not n: return [-1,-1]
  if n == 1 :
    if nums[0] == t : return [0,0]
    else : return [-1, -1]
  
  pL = 0; pR = n-1
  while pL <= pR: 
    pM = (pR + pL) / 2
    if nums[ pM ] == t:
      anchor = nums[pM]
      ppL = ppR = pM
      while ppL >= 0 :
	if nums[ ppL ] != anchor: break
	ppL -= 1
      while ppR <= n-1 :
	if nums[ ppR ] != anchor: break
	ppR += 1
      return [ppL+1, ppR-1]	

    elif nums[pM] > t: pR = pM - 1 
    else: pL = pM + 1
  return  [-1, -1]

print [3,4], searchRange([5, 7, 7, 8, 8, 10], 8)
print [3,5], searchRange([5, 7, 7, 8, 8, 8], 8)
print [0,0], searchRange([5, 7, 7, 8, 8, 10], 5)
print [-1,-1], searchRange([5, 7, 7, 8, 8, 10], 9)
print [-1,-1], searchRange([5, 7, 7, 8, 8], 9)
print [-1,-1], searchRange([5], 9)
print [0,0], searchRange([5], 5)
print [-1,-1], searchRange([], 5)

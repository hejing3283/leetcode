# @param {integer[]} nums
# @param {integer} target
# @return {integer} 
def search(nums, t):
  n = len(nums)
  if not n : return -1
  if n == 1:
    if nums[0] == t: return 0
    else : return -1

  pL = 0
  for i in range(1,n):
    if nums[i] < nums[i-1] :
      pL = i
  pR = pL + n - 1
  while pL <= pR :
    pM = (pL + pR) / 2 
    if nums[pM % n] > t :
      pR = pM - 1
    elif nums[pM % n ] < t :
      pL = pM  + 1
    else :
      return pM % n 

  return -1

print 3, search([4,5,6,0,1,2],0) 
print 6, search([4,5,6,0,1,2,3],3) 
print 0, search([4,5,6,0,1,2,3],4) 
print 2, search([4,5,6,0,1,2,3],6) 
print 1, search([4,5,6,0,1,2,3],5) 
print 5, search([4,5,6,0,1,2,3],2) 
print -1, search([4,5,6,0,1,2,3],7) 
print 0, search([1],1) 
print -1, search([1,3],0) 

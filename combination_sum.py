# @param {integer[]} candidates
# @param {integer} target
# @return {integer[][]}
def combinationSum(candidates, t):

  def help(a, t, cur, s, ans):
    if t == 0: 
      ans.append(cur[:])
    if t < 0 or a[s] > t: 
      return [] 
    while s < len(a) :
      cur.append(a[s])
      r = help(a, t - a[s], cur, s, ans)
      cur.pop()
      if t - a[s] < 0 :
	break
      s += 1

  candidates.sort() 
  if not candidates or t < candidates[0]: return []
  elif candidates[0] == t: return [[candidates[0]]]
  else:
    ans  = []
    help(candidates, t, [], 0, ans) 
    return ans
    
print combinationSum([2,3,6,7],7)
print combinationSum([2,5,6,7,8],7)
print combinationSum([8,9,10],7)
print combinationSum([1,2,3,4],0)
print combinationSum([1,2,3,4],1)
print combinationSum([],0)

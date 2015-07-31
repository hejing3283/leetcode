def permute(nums):
  if len(nums) == 0: return []
  if len(nums) == 1: return [nums]
  ans = []
  for i in range( len(nums) ):
    for j in permute( nums[:i] + nums[i+1:] ):
      ans.append( [nums[i]] + j )
  return ans

print permute([1,2,3])
print permute([])
# print [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2],[3,2,1]

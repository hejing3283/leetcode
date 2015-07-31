class Solution(object):
  # @param {integer[]} nums
  # @return {integer[][]}
  def permuteUnique(self, nums):
    nums.sort()
    ans = []
    if len(nums) == 0: return []
    if len(nums) == 1: return [nums]
    prev = None
    for i in range(len(nums)):
      if nums[i] == prev: continue
      prev = nums[i]
      for j in self.permuteUnique( nums[:i] + nums[i+1:] ):
	ans.append( [nums[i]] + j  )
    return ans

sol = Solution()
print sol.permuteUnique([1,1,2])
print sol.permuteUnique([1,1,1,1])
print sol.permuteUnique([])
		        

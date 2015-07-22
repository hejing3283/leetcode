class Solution:
  # @param {integer[]} nums
  # @param {integer} target
  # @return {integer[]}
  def twoSum(self, nums, target):
    out = {}
    for ia in range(len(nums)):
      if target - nums[ia] in out.keys():
	return out[ target - nums[ia] ] + 1, ia + 1
      out[ nums[ia] ] = ia

    
  

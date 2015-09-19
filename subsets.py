class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start, nums, depth, valueList) :
            res.append(valueList)
            if depth == len(nums):return 
            for i in range( start, len(nums) ) :
                dfs( i + 1, nums, depth+1, valueList + [nums[i]] ) 
        nums.sort()
        res = []
        dfs(0, nums, 0, [] )
        return res
        
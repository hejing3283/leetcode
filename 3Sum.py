class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ### do specific for 3 sums; 196ms 
        if len(nums) < 3: return []
        nums.sort()
        
        l = len(nums); ans = []
        for i in range(l-2):
            first = nums[i]
            if i > 0 and nums[i-1] == first:    continue 
            left = i + 1; right =  l - 1 
            sum2 = 0 - first 
            while left < right:
                curr = nums[left] + nums[right] 
                if curr == sum2:
                    ans.append([ first, nums[left], nums[right] ] ) 
                    left += 1; right -= 1 
                    while ( left < right and nums[left] == nums[left-1] ) : left += 1 
                    while ( left < right and nums[right] == nums[right +1 ]) : right -=1
                elif curr > sum2:
                    right -=1
                else:
                    left += 1 
        return ans 
            
        ### take the n-sums solution AC 1 420 ms
        # target = 0 
        # def nSums( nums, target, N, curr, res):
        #     if N < 2 or len(nums) < N: return 
        #     if N == 2 :
        #         l ,r = 0, len(nums)-1
        #         while l < r:
        #             if nums[l] + nums[r] == target:
        #                 res.append( curr + [ nums[l], nums[r] ] ) 
        #                 r -= 1 ; l += 1 
        #                 while l < r and nums[l] == nums[l-1]: l+= 1 
        #                 while l < r and nums[r] == nums[r+1]: r-= 1 
        #             elif nums[l] + nums[r] < target:
        #                 l += 1 
        #             else:
        #                 r -= 1 
        #     else:
        #         for i in range(0, len(nums) - N + 1 ) :
        #             if target < nums[i] * N  or target > nums[-1] * N: break 
        #             if i == 0 or ( i > 0 and nums[i-1] != nums[i] ):
        #                 nSums( nums[i+1:], target - nums[i], N -1, curr + [nums[i]], res ) 
        #     return 
        # nums.sort()
        # res = []
        # nSums( nums, 0 , 3, [] , res)
        # return res 
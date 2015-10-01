class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ### time limited reached
        # maxEndIdx = 0
        # maxSoFar = nums[0]
        # for i in range(1, len(nums)) :
        #     cur = nums[i]; j = i
        #     tmpIdx = maxEndIdx 
        #     while j >= maxEndIdx:
        #         if cur > maxSoFar: 
        #             maxSoFar = cur
        #             tmpIdx = j 
        #         j -= 1 ;
        #         cur *= nums[j]
        #     maxEndIdx = tmpIdx
        # return maxSoFar
        
        ## dp   
        maxP, minP, res = nums[0], nums[0], nums[0];
        for i in range(1, len(nums)) :
            _maxP = maxP; #_minP = minP
            maxP = max( max( _maxP * nums[i], nums[i]), minP * nums[i]) 
            minP = min( min( _maxP * nums[i], nums[i]), minP * nums[i]) 
            res = max( res, maxP ) 
        return res
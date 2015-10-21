class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        unique = dict()
        for i in xrange(len(nums)):
            num = nums[i]
            if num in unique:
                for idx in unique[num]:
                    if i - idx <= k :
                        return True
                unique[num].append(i) 
            unique[num] = [i] 
        return False 
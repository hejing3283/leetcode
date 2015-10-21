class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ### another method is to try the linked-list with cycle method
        n = len(nums)
        left, right = 0, n-1
        while right >= left:
            
            mid = (left + right) / 2
            count = sum( x <= mid for x in nums )
            if count > mid :
                right = mid - 1
            else :
                left = mid + 1
        return left

            
        
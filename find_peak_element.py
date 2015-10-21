class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1 
        n = len(nums)
        MIN_VALUE=-10000000000
        def binSearch( nums, left, right ) :
            # if right >= left and left >=0 and right <n:
            if right < left: return 'null'
            mid = (left + right)/2
            a = nums[mid-1] if mid > 0 else MIN_VALUE
            b = nums[mid+1] if mid < n-1 else MIN_VALUE
            if nums[mid] > a and nums[mid] > b:
                    return mid 
            ans = binSearch(nums, left, mid-1)
            if ans != 'null' :
                return  ans
            else:
                return binSearch(nums, mid+1, right)
        return binSearch(nums, 0, n-1) 
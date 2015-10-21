class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique  = set()
        for x in nums:
            if x not in unique:
                unique.add(x)
            else :
                return True 
        return False 
        
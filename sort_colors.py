class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            p0 = 0 ; p2 = len(nums) - 1 ; pcur = 0
            while pcur <= p2   :
                if nums[pcur] == 0 : 
                    nums[pcur],  nums[p0] = nums[p0], nums[pcur]
                    p0 += 1
                    pcur += 1 
                elif nums[pcur] == 2 : 
                    nums[pcur], nums[p2] = nums[p2], nums[pcur]
                    p2 -= 1
                else:
                    pcur += 1  
            
            
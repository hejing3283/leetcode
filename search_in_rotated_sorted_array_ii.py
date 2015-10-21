class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l, r = 0, len(nums)-1
        
        while l < r:
            mid = l + (r-l)/2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r]:
                # right side in order
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                ## left side in order
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                ### duplicates, only move right, to keep inclusive
                r -= 1
        return nums[l] == target
        
        #### problem with boundary cases
        # def nextDistinct( nums, p):
        #     prev = nums[p]; pl = pr = p 
        #     while pl >= 0 and pr < len(nums)-1:
        #         if nums[pl] == prev: pl -= 1
        #         elif nums[pr] == prev: pr += 1
        #         else:
        #             break
        #     if pl!=p:
        #         pl +=1
        #     if pr != p:
        #         pr -+1
        #     return pl, pr
            
        # def bSearch( nums, left, right ):
 
        #     mid = (left + right) / 2
        #     ml, mr = nextDistinct(nums, mid) 
        #     _, left = nextDistinct(nums, left)
        #     right, _ = nextDistinct(nums, right) 
        #     ml  = max(left, ml); mr = min(mr, right)
            
        #     print nums[mid], left, ml, mr, right
        #     if not right > left : 
        #         return target == nums[left]
        #     if nums[mid] == target: return True
                    
        #     if nums[ml] > nums[left]:
        #         if target >= nums[mr]:
        #             return bSearch( nums, mr, right)
        #         else:
        #             return bSearch( nums, left, ml-1)
        #     else:
        #         if target > nums[right]:
        #             return bSearch( nums, left, ml)
        #         else:
        #             return bSearch( nums, mr, right )

        # if not nums: return not target
        # return bSearch(nums, 0, len(nums)-1)
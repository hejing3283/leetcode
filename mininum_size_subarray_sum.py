class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        ### O(nlogn) from web
        ### nlogn is typical tree, binary 
        n = len(nums); n1= n+1 
        sums = [0 for _ in range (n1) ]
        for i in range(n):
            sums[i+1]  = nums[i] + sums[i]
        
        ans = n1;  
        for left in range( n1 ) :
            right = self.binSearch( sums, left+1, n, sums[left] + s ) 
            if right == n1 :   
                break
            ans = min( ans, right - left)  ### doing a min oprations everytime better then doing a if and the assigment
        return ans if ans != n1 else 0 
        
    def binSearch(self, sums, left, right, key):
        while left <= right:
            mid = (left  + right) / 2 
            if sums[mid] >= key : right = mid - 1 
            else:
                left = mid + 1
        return left 
                    
        
        # ### O(n) from web: same idea, just keep the order
        # if not nums: return 0 
        # left, right = 0, 0; ans = len(nums) + 1; sums = 0 
        # while right < len(nums) :
        #     while right < len(nums) and sums < s  : 
        #         sums += nums[right];  right += 1 
        #     while sums >= s :
        #         # print left, right 
        #         ans = min(ans, right - left) 
        #         sums -= nums[left]
        #         left += 1 
        # return ans if ans != len(nums) + 1 else 0      
        
        #### to find the subarray, not sorting in place and find the element
        #### get to know the meaning of the problem!!!!
        # if not nums: return 0 
        # nums.sort(reverse = True) 
        
        # ans = len(nums) + 1   
        # for slow in range(len(nums)): 
        #     if s <= nums[slow]: 
        #         return 1 
        #     fast = slow + 1
        #     curr = 1; ss = s - nums[slow] 
             
        #     for fast in range(slow+1, len(nums)):
        #         if ss <= nums[fast] :
        #             ss -= nums[fast]
        #             curr += 1 
        #             ans = min(ans, curr) 
        #             break
        #         else:
        #             ss -= nums[fast]
        #             curr += 1
        #     # print curr, ans 
        # return ans 
                        
            
# @param {integer[]} nums
# @return {void} Do not return anything, modify nums in-place instead.
def nextPermutation(nums):
 N = len(nums)
 pnum = []; p = N 
 prev = nums[-1]; i = N - 1 
 while i >= 0 :
   if nums[i] < prev:
     p = i
     break
   else:
     prev = nums[i]
   i -= 1
 if i == -1:
   p =  N-1
   pnum = nums[p]
   nums[::] = nums[::-1]
   return 
 else:
   i =  N - 1
   while i > p :
     if nums[i] > nums[p]:
       exnum = nums[i]
       ex = i
       break
     i -= 1
   nums[p], nums[ex] = nums[ex], nums[p]
   nums[::] = nums[:(p+1)] + nums[(p+1):][::-1]
   return 

nums = range(5)
print nums,"-", 
nextPermutation(nums) 
print nums
nums = [1,2,3] 
print nums,"-",
nextPermutation(nums) 
print nums

nums = [3,2,1] 
print nums,"-",
nextPermutation(nums) 
print nums
nums = [1,1,5] 
print nums,"-",
nextPermutation(nums) 
print nums

nums = [1,3,2] 
print nums,"-", 
nextPermutation(nums) 
print nums
# nums = [6,8,7,4,3,2] 
# print nums,"-", 
# nextPermutation(nums) 
# print nums



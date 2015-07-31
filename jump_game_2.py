# @param {integer[]} nums
# @return {integer}
def jump(nums):
  nsteps = curr = last = 0 
  for i in range(len(nums)):
    if i > last:
      last = curr
      nsteps += 1
    curr = max(curr, i + nums[i])
  return nsteps

print jump([2,3,1,1,4]), 2

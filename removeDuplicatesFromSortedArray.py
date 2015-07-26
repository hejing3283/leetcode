def removeDuplicates(nums):
  if not nums :
    return 0
  prev = nums[0]; i = 1
  while i < len( nums ):
    if nums[i] == prev:
      nums.pop(i)
    else:
      prev = nums[i]
      i += 1
  return i

print removeDuplicates([0,1,1,2])
print removeDuplicates([])
print removeDuplicates([1,1,1,1])
print removeDuplicates([1])

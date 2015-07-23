def plusOne(digits):
  # for i in range(len(digits)-1,-1,-1):
  if not digits:
    return 0
  i = len(digits)-1 
  head = 1
  while head and i >= 0 :
    temp = digits[i] + head
    head = temp / 10
    digits[i] = temp % 10
    i -= 1
  if head :
     return [1] + digits
  else:
    return digits


print '234',    plusOne([1,2,3])
print '1240',   plusOne([1,2,3,9]) 
print '10',	plusOne([9] )  
print '10000',  plusOne([9,9,9,9]) 
print '1',	plusOne([0]) 
print '0',	plusOne([]) 


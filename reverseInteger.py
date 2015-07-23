def reverse(x):
  import math
  x = int(x)
  ret = 0
  sign = math.copysign(1,x)
  x = abs(x)
  while x:
    if ret > 214748364 :
      return 0
    ret = ret * 10 + x % 10
    x = x // 10
  return int(ret * sign) 

print 321, reverse(123)
print -321, reverse(-123)
print -1, reverse(-10000)
print 3, reverse(3)
print 0, reverse(10000000003)


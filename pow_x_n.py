class Solution:
  # @param {float} x
  # @param {integer} n
  # @return {float}
  def myPow(self, x, n):
    '''
    divide and conquer
    overlow, underflow, sign, 0 
    '''
    OVERFLOW = 200000000000
    UNDERFLOW = -20000000000
    if n == 0: return 1 
    if n < 0 : x = 1.0/x; n = abs(n); sign = -1
    if n == 1: return x
    if abs(x) == 1: return (x * x if n%2 else x)
    if x == 0.0 or x == 0: return 0 

    ans = 1; i = 1
    while i <= n :
      ans = ans * x * x 
      i += 2
      if ans > OVERFLOW:
	return OVERFLOW
      elif ans < UNDERFLOW:
	return UNDERFLOW

    return ans

sol = Solution()
# print sol.myPow(0.1,-1)
# print sol.myPow(10000,0)
# print sol.myPow(1,100)
# print sol.myPow(3,2)
# print sol.myPow(3,-2)
print sol.myPow(2,-10)


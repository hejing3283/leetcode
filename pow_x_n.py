class Solution:
  # @param {float} x
  # @param {integer} n
  # @return {float}
  def myPow(self, x, n):
    '''
    divide and conquer
    overlow, underflow, sign, 0 
    '''
    if abs(x) == 1: return (x * x if n%2 else x)
    if x == 0 : return 0 
    if n == 0: return 1 
    ans = 0; 
    if n < 0 : 
      x = 1/x; n = abs(n)
    while i <= n :
      ans += x * x 
      i += 2
      if ans > OVERLOW:
	return OVERFLOW
      elif ans < UNDERFLOW:
	return UNDERFLOW

    return ans

sol = Solution()
print sol.myPow(0.1,-0.1)
print sol.myPow(10000,0)
print sol.myPow(1,100)


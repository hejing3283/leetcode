class Solution:
  # @param {float} x
  # @param {integer} n
  # @return {float}
  def myPow(self, x, n):
    '''
    divide and conquer
    overlow, underflow, sign, 0 
    '''
    if n == 0: return 1 
    if n < 0 : x = 1.0/x; n = - n; 
    if n == 1: return x
    if x == -1: return (-1 if n%2 else 1)
    if x == 0.0 or x == 0: return 0 

    ans = 1; 
    while n :
      if n & 1:
	ans = ans * x 
      x *= x
      n >>= 1
    return ans

sol = Solution()
print sol.myPow(0.1,-1)
print sol.myPow(10000,0)
print sol.myPow(1,100)
print sol.myPow(3,2)
print sol.myPow(3,-2)
print sol.myPow(2,-10)
print sol.myPow(-1.00000, 2147483647)
print sol.myPow(1.00000, 2147483647)


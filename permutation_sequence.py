class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        fac = 1
        k -= 1
        for i in range(1,n): fac *= i 
        
        nums = range(1,10) 
        for i in reversed( range(n) ) :
            print k, i, fac
            curr = nums[ k / fac ]
            res += str(curr)
            nums.remove(curr)
            
            if i != 0 :
                k %= fac 
                fac /= i 
        return res
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ### method 1 
        # ans = 0
        # if n < 2 : return ans
        # for i in range(2,n):
        #     if self.isPrime(i): ans += 1
        # return ans 
        
        ### method 2 
        # return self.isPrime_2(n)
        
        return self.countPrimes_3(n)

        
    def isPrime(self, n ):
        ### TLE
        if n < 2: return False  
        i = 2
        while i * i <= n:
            if not n % i : return False 
            i += 1
        return True
        
    def isPrime_2(self,n):
        ### Memory Limite
        marked = dict()
        for i in xrange(n):
            marked[i] = True
        i = 2
        while i*i < n:
            if not marked[i]: i += 1; continue 
            j = i*i 
            while j < n:
                marked[j] = False 
                j += i 
            i += 1
        ans = 0 
        for i in xrange(n):
            if marked[i] : ans += 1
        return ans
        
    def countPrimes_3(self, n ):
        ### from web, AC version
        if n < 3 : return 0 
        ans = [True] * n 
        nums = range(1,n,2)
        nums[0] = 0 ; ans = 1
        n //= 2
        for i in itertools.ifilter(None,nums):
            ans += 1 
            for j in xrange(i * i // 2, n, i) :
                nums[j] = 0  
                    
        return ans
        
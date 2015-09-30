class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ### list to handle:
        # if x > 2147483648 or x < - 2147483647 or x < 0: return False 
        # x = list( str(x) ) ; n = len(x)
        # i = 0 ; j = n-1
        # while i<j:
        #     if x[i] == x[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         return False 
        # return True 
        
        if x > 2147483648 or x < - 2147483647 or x < 0: return False 
        revNum = 0 ; old = x 
        while x > 0 :
            temp = x % 10
            revNum = revNum * 10 + temp
            x = x/10
        return (True if revNum == old else False) 
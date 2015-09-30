class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        vals =    [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] 
        symbols = ['M','CM','D','CD','C','XC', 'L','XL','X','IX','V','IV','I']
        i = 0 ; res = ''
        print i, num
        while num > 0 : 
            k = num / vals[i] 
            if k > 0 :
                for j in range(k) :
                    res += symbols[i]
                    num -= vals[i]
            i += 1
        return res
            
        
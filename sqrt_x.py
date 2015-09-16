class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = abs(x)
        if x < 2 : return x 
        left = 1; right = ( x / 2 + 1)
        i = left 
        while i < right  :
            temp = i * i
            if temp > x:
                right = i 
                left = i / 2
                break
            elif temp == x : 
                return i 
            i *= 2
            
        while right - left > 1 : 
            med = (right + left ) / 2
            temp = med * med
            if  temp > x :
                right = med 
            elif temp < x : 
                left = med 
            else:
                return med
            
        return left 
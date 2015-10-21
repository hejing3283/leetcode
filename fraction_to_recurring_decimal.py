class Solution(object):
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        if d == 0 : return 'Inf' if n >= 0 else '-Inf'
        sign = '-' if n * d < 0 else ''        
        n, d = abs(n),abs(d)
        head, n = divmod( n, d) ### replace n makes is faster
        tail, see = '', {}
        while n > 0 : 
            if n in see :
                tail = tail[: see[n]] + "(" + tail[see[n]:] + ")" 
                break
            see[n] = len(tail)
            digit, n = divmod( n * 10, d) 
            tail += str(digit)

        return sign + str(head) + (tail and "." + tail)

            
            
            
        
        
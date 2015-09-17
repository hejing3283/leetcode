class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ## 1, 0  ->1 , 0, 0 -> 0, 1,1-> 0, 1 
        carry = 0
        a = a[::-1]
        b = b[::-1]
        i = j = 0 
        res = ''
        while i < len(a) and j < len(b):
            curr = int(a[i]) + int( b[j] ) + carry
            carry = curr / 2
            res = str(curr % 2 ) + res
            i += 1; j += 1
        while i < len(a):
            curr = int(a[i]) + carry
            carry = curr / 2
            res = str(curr % 2 ) + res
            i += 1
        while j < len(b):
            curr = int( b[j] ) + carry
            carry = curr / 2
            res = str(curr % 2 ) + res
            j += 1
            
        if carry == 1:
            res = '1' + res
        return res
                    
            
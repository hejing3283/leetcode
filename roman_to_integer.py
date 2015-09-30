class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals =    [1000, 900, 500, 400, 100, 90, 50,40,10, 9, 5, 4, 1] 
        symbols = ['M',  'CM', 'D', 'CD',  'C', 'XC', 'L','XL','X','IX', 'V','IV','I'  ]
        myDict = dict(zip(symbols, vals))
        
        prev, i = s[0], 1 
        res = myDict[ prev] 
        while i < len(s)  : 
            curr = s[i]
            if myDict[prev] < myDict[ curr ]:
                res += myDict[ curr ] - 2 * myDict[ prev ] 
            else:
                res += myDict[ curr ]
            prev = curr ; i += 1 
        return res 
        
        
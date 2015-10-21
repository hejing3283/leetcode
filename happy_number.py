class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev = n ; curr = 0
        midDict = dict()
        while True :
            curr += (prev % 10) ** 2
            prev = prev / 10 
            if prev == 0:
                if curr == 1: 
                    return True
                tmp = midDict.get(curr,None)
                if not tmp:
                    midDict[curr] = 1
                else:
                    return False
                prev, curr = curr, 0 
        return False 
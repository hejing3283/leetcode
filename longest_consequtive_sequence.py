class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for i in nums: mydict[i] = False
        res = 0 ; 
        for i in nums:
            if  not mydict[i] : 
                mydict[i] = True
                cur = 1 ; j = 1
                while  i+j in mydict and not mydict.get(i+j, False) :
                    mydict[i+j] = True; j += 1; cur += 1
                j = 1
                while i - j in mydict and not mydict.get(i-j, False):
                    mydict[i-j] = True; j += 1; cur += 1
                res = max(res, cur) 
        return res
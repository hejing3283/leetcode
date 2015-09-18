class Solution(object):
    def maximalRectangle(self, M):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0 
        if not M : return res
        
        tmp = [ 0 for j in range(len(M[0])) ] 
        for i in range( len(M) ) :
            for j in range( len(M[0]) ):
                tmp[j] = (tmp[j] + 1 if M[i][j] == '1' else 0 )
            tmpAera = self.searchMaxAera( tmp ) 
            res = tmpAera if tmpAera > res else res
        return res 
                
    def searchMaxAera(self, nums ) : 
        idxStack = []; hStack = []; maxAera = 0; 
        for i in range(len(nums)):
            if hStack == [] or hStack[-1] < nums[i]:
                hStack.append( nums[i] ) ; idxStack.append(i) 
            else:
                if hStack and hStack[-1] > nums[i]:
                    lastIdx = 0 
                    while hStack and hStack[-1] > nums[i] :
                        lastIdx = idxStack.pop()
                        tmpAera = hStack.pop() * (i - lastIdx) 
                        maxAera = tmpAera if tmpAera > maxAera else maxAera
                    hStack.append( nums[i] ); idxStack.append( lastIdx )
        while hStack:
            tmpAera = hStack.pop() * (len(nums) - idxStack.pop())
            maxAera = tmpAera if tmpAera > maxAera else maxAera
        return maxAera 
class Solution(object):
    def largestRectangleArea(self, H):
        """
        :type height: List[int]
        :rtype: int
        """
        hStack = []
        idxStack = []
        maxAera = 0 
        for i in range(len(H)): 
            if hStack == [] or hStack[-1] < H[i]:
                hStack.append( H[i] )
                idxStack.append( i )
            elif hStack[-1] > H[i] :
                lastIdx = 0 
                while hStack and hStack[-1] > H[i]:
                    lastIdx  = idxStack.pop()
                    currAera = hStack.pop() * ( i - lastIdx )
                    if currAera > maxAera : maxAera = currAera
                hStack.append( H[i] ) ; idxStack.append( lastIdx ) 

        while hStack:
            currAera = hStack.pop() * ( len(H) - idxStack.pop() ) 
            maxAera = currAera if currAera > maxAera else maxAera 
        return maxAera 
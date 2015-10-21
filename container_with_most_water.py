class Solution(object):
    def maxArea(self, H):
        """
        :type height: List[int]
        :rtype: int
        """
        ## similar as water trap
        
        if len(H) < 2: return 0 
        n = len(H)
        l, r = 0 , n - 1
        
        maxA = 0
        while l < r:
            if H[l] > H[r]: 
                curr = H[r] * (r -l)
                r -= 1
            elif H[l] < H[r]:
                curr = H[l] * ( r- l ) 
                l += 1 
            else:
                curr = H[l] * ( r- l ) 
                l += 1 
                r -= 1 
            maxA = max(curr, maxA)
        return maxA 
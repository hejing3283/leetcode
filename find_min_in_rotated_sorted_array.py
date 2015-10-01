class Solution(object):
    def findMin(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        L, R = 0, len(A) -1 
        while L < R and A[L] >= A[R] :
            M = ( L + R ) / 2 
            if A[M] > A[R]:
                L = M + 1
            else:
                R = M 
        return  A[L]
        
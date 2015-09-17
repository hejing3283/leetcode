class Solution(object):
    def searchMatrix(self, M, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0 ; j = len(M[0]) - 1
        while i < len(M) and j >= 0:
            if M[i][j] == target : return True
            elif M[i][j] < target:  i += 1
            else : j -= 1
        return False
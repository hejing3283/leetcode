class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ## DP
        n = len(grid[0])
        m = len(grid) 
        if m == 0 or n == 0 : return 0
        dummy = [ [0 for j in range(0,n+1)] for i in range(0,m+1) ] 
        dummy[0][0] = grid[0][0]
        for i in range(1,m) : dummy[i][0] = dummy[i-1][0] + grid[i][0]
        for j in range(1,n) : dummy[0][j] = dummy[0][j-1] + grid[0][j]
        for i in range(1,m+1):
            for j in range(1, n+1):
                dummy[i][j] = grid[i-1][j-1]
          
        for j in range(1,n):
            for i in range(1,m):
                dummy[i][j] = min( dummy[i-1][j], dummy[i][j-1]) + grid[i][j] 
        return dummy[m-1][n-1]
        
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0]) 
        m = len(obstacleGrid) 
        list = [ [0 for j in range(n) ] for i in range(m) ] 
        
        for j in range(n) :
            if obstacleGrid[0][j] == 1 :
                list[0][j] = 0
                break
            else:
                list[0][j] = 1
        for i in range(m) :
            if obstacleGrid[i][0] == 1 :
                list[i][0] = 0
                break
            else:
                list[i][0] = 1
        for i in range(1, m ):
            for j in range( 1, n) : 
                if obstacleGrid[i][j] == 1:
                    list[i][j] == 0
                else:
                    list[i][j] = list[i-1][j] + list[i][j-1]
        return list[m-1][n-1] 
        
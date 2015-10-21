class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon: return 1
        m = len(dungeon) ; n = len(dungeon[0])
        dp  = [ [ 0 for _ in range(n)] for __ in range(m) ] 
        dp[m-1][n-1] = max(0, -dungeon[m-1][n-1] ) + 1
        for x in range(m-1, -1,-1):
            for y in range(n-1, -1,-1):
                right = None; down  = None
                if x + 1 < m :
                    down = max(1, dp[x+1][y] - dungeon[x][y])
                if y + 1 < n :
                    right = max(1, dp[x][y+1] - dungeon[x][y])
                if down and right:
                    dp[x][y] = min(down,right)
                elif down:
                    dp[x][y] = down
                elif right:
                    dp[x][y] = right
        return dp[0][0]
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        if n == 1: return [[1]]
        up = left = 0  
        down = right = n-1
        res = [ [ 0 for i in range(n)] for j in range(n) ]
        curr = 0
        direction = 0 ;
        while True: 
            if direction == 0 :
                for i in range(left, right + 1 ) :
                    curr += 1; res[up][i] = curr 
                up += 1
            elif direction == 1:
                for i in range(up, down + 1 ) :
                    curr += 1; res[i][right] = curr 
                right -= 1
            elif direction == 2:
                for i in range(right, left - 1, -1 ) :
                    curr += 1; res[down][i] = curr 
                down -= 1
            elif direction == 3:
                for i in range(down, up - 1, -1 ) :
                    curr += 1; res[i][left] = curr
                left += 1
            direction = (direction + 1) % 4 
            if curr == n * n  : return res
            
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #### 2 loops
        
        if not matrix: return False
        y = len(matrix[0]) - 1 
        for x in  range(len(matrix)):
            while y and matrix[x][y] > target:
                y -= 1
            if matrix[x][y] == target:
                return True 
        return False 
        
        # ### binary search
        # def binSearch( nums, low, high, t) :
        #     while low <= high: 
        #         mid = (low + high) / 2 
        #         if t >= nums[mid]:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #     return high 
        # if not matrix: return False 
        # y = len(matrix[0]) -1 
        # for x in range(len(matrix)):
            
        #     y = binSearch(matrix[x][:], 0, y, target)
        #     if matrix[x][y] == target:
        #         return True
        # return False 
            
        
        # nrow = len(matrix);
        # if not matrix: return False
        # ncol = len(matrix[0])
        # sr, sc, er, ec = 0, 0, nrow-1, ncol-1
        # # while er > sr and ec > sc : 
        # midRow = (sr + er) / 2
        # midCol = (sc + ec) / 2
        # # print sr,er, sc, ec
        # if target == matrix[ midRow][midCol] :
        #     return True
        # elif target > matrix[midRow][midCol]  :
        #     return self.searchMatrix( matrix[sr:midRow][midCol: ncol] , target) or self.searchMatrix( matrix[midRow:][:], target )
            
        # elif target < matrix[midRow][midCol]:
        #     return self.searchMatrix( matrix[:midRow][:] , target) or self.searchMatrix( matrix[midRow:][:midCol], target )
        # else:
        #     return False 
        
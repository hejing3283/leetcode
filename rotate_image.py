class Solution():
  # @param {integer[][]} matrix
  # @return {void} Do not return anything, modify matrix in-place instead.
  def rotate(self, matrix):
    n = len(matrix) - 1
    center = (n +1)/ 2  #+ n % 2
    for i in range(center):
      for j in range(center):
	#lt =  
	tmp = matrix[i][j] 
	matrix[i][j]     = matrix[ n-i ][ j ]
	#lb = 
	matrix[n-i][j]   = matrix[ n-i ][ n-j ]
	#rb 
	matrix[n-i][j] = matrix[ n-i ][ n-j ]
	#rt = 
	matrix[n-i][n-j] = matrix[i][n-j]
	matrix[i][n-j] = tmp 
    print matrix
     





	    

sol = Solution()
# sol.rotate([[1,3,4,5],[1,2,3,1],[6,4,5,6],[2,3,1,1]])
sol.rotate([[1,3,4],[2,3,1],[6,5,6]])


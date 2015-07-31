class Solution():
  # @param {integer[][]} M
  # @return {void} Do not return anything, modify M in-place instead.
  # def rotate(self, M):
  #   n = len(M) - 1
  #   center = (n +1)/ 2  #+ n % 2
  #   print center
  #   for i in range(center  ):
  #     for j in range(center ):
	# tmp = M[i][j] 
	# M[i][j]     = M[ n-i ][ j ]
	# M[n-i][j]   = M[ n-i ][ n-j ]
	# M[n-i][n-j] = M[i][n-j]
	# M[i][n-j] = tmp 
  #   if len(M) % 2 == 1:
	# for i in range(center):
	  # tmp = M[i][center] 
	  # M[i][center]     = M[ n-center ][ i ]
	  # M[n-center] [i]  = M[ n-i ][ n-center ]
	  # M[n-i][n-center] = M[center][n-j]
	  # M[center][n-j] = tmp 
  def rotate(self, M):
    n = len(M)
    for i in range(n):
      for j in range(i+1, n):
	M[i][j], M[j][i] = M[j][i], M[i][j]
    for i in range(n):
      M[i].reverse()
    # print M
     





	    

sol = Solution()
sol.rotate([[1,3,4,5],[1,2,3,1],[6,4,5,6],[2,3,1,1]])
# sol.rotate([[1,3,4],[2,3,1],[6,5,6]])
sol.rotate([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]])


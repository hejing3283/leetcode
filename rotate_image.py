class Solution():
  # @param {integer[][]} M
  # @return {void} Do not return anything, modify M in-place instead.
  def rotate(self, M):
    n = len(M)
    for i in range(n):
      for j in range(i+1, n):
	M[i][j], M[j][i] = M[j][i], M[i][j]
    for i in range(n):
      M[i].reverse()
     





	    

sol = Solution()
sol.rotate([[1,3,4,5],[1,2,3,1],[6,4,5,6],[2,3,1,1]])
sol.rotate([[1,3,4],[2,3,1],[6,5,6]])
sol.rotate([[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]])


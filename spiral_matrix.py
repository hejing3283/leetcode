class Solution:
  # @param {integer[][]} matrix
  # @return {integer[]}
  def spiralOrder(self, M):
    ans = []
    up = 0; left = 0;
    
    down = len(M) - 1
    if down < 0 : return M 
    right = len(M[0]) - 1 ; 

    direction  = 0 # 0: right; 1 : down; 2: left; 3: up; 
    res = []
    while True :
      if direction == 0:
	for i in range(left, right+1):
	  ans.append( M[up][i] )
	up += 1
      elif direction == 1:
	for i in range(up, down+1):
	  ans.append( M[i][right] )
	right -= 1
      elif direction == 2:
	for i in range(right, left-1, -1):
	  ans.append( M[down][i] )
	down -= 1
      elif direction == 3:
	for i in range(down, up-1, -1):
	  ans.append( M[i][left] )
	left += 1
      if left > right or up > down: return ans
      direction = ( direction + 1 ) % 4

sol = Solution()
m = [ [ 1, 2, 3 ],
      [ 4, 5, 6 ],
       [ 7, 8, 9 ] ]
print sol.spiralOrder(m)
m = [ [ ] ] 
print sol.spiralOrder(m)
m = [ [1] ] 
print sol.spiralOrder(m)
m = [ [1,2,3] ] 
print sol.spiralOrder(m)
m = [ [1],[2],[3] ] 
print sol.spiralOrder(m)


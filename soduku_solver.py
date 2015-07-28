def solveSudoku(b):
  # @param {character[][]} board
  # @return {boolean}
  def isValid(x,y):
    tmp = b[x][y]; b[x][y] = 'D'
    for i in range(9):
      if b[i][y] == tmp: return False
    for i in range(9):
      if b[x][i] == tmp: return False
    for i in range(3):
      for j in range(3):
	if b[x/3 * 3 + i][y/3 * 3 + j] == tmp: return False 
    b[x][y] = tmp
    return True
  
  def dfs(b):
    for i in range(9):
      for j in range(9):
        if b[i][j] == '.':
          for k in '123456789':
            b[i][j] = k
            if isValid(i, j) and dfs(b): 
	      return True
            b[i][j] = '.'
	  return False
    return True
  dfs(b)

b = [['5','3','.','.','7','.','.','.','.'],
     ['6','.','.','1','9','5','.','.','.'],
     ['.','9','8','.','.','.','.','6','.'],
     ['8','.','.','.','6','.','.','.','3'],
     ['4','.','.','8','.','3','.','.','1'],
     ['7','.','.','.','2','.','.','.','6'],
     ['.','6','.','.','.','.','2','8','.'],
     ['.','.','.','4','1','9','.','.','5'],
     ['.','.','.','.','8','.','.','7','9']]
print solveSudoku(b) 
print b

def combinationSum2(candidates, target): 
  ans = []
  candidates.sort()
  def DFS(c, t, start, cur):
    length = len(c)
    if t == 0 and cur not in ans:
      return ans.append(cur)
    for i in range(start,length):
      if t < c[i]: 
        return 
      DFS(c, t - c[i], i+1, cur + [c[i]])

  DFS(candidates, target, 0, [])
  return ans 

print [[1,7],[1,2,5],[2,6],[1,1,6]], "<==", combinationSum2([10,1,2,7,6,1,5],8)
print combinationSum2([10,1,2,7,6,1,5],1)
print combinationSum2([10,1,2,7,6,1,5],0)
print combinationSum2([10,1,2,7,6,1,5],11)
print combinationSum2([10],11)
print combinationSum2([10],10)
print combinationSum2([],10)

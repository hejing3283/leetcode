class Solution:
  # @param {string[]} strs
  # @return {string[]}
  def anagrams(self, strs):
    strs.sort()
    if len(strs) == 0: return []
    if len(strs) == 1: return [strs]
    prev = ''; ans = []
    for i in range(len(strs)):
      if strs[i] == prev: 
	prev = strs[i]
	continue
      for j in self.anagrams( strs[:i] + strs[i+1:]):
	ans.append([strs[i]] + j ) 
    return ans

sol = Solution()
print sol.anagrams(['a','b','c'])
		        

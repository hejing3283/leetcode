class Solution:
  # @param {string[]} strs
  # @return {string[]}
  def anagrams(self, strs):
    strs.sort()
    strs = [ s for s in strs if s]
    if len(strs) == 0: return [''] 
    if len(strs) == 1: return strs
    prev = None; ans = []
    for i in range(len(strs)):
      if strs[i] == prev:  continue
      prev = strs[i];
      for j in self.anagrams( strs[:i] + strs[i+1:]):
	ans.append(strs[i] + j) 
    return ans

sol = Solution()
print sol.anagrams(['a','b','c'])
print sol.anagrams(['a','c','c'])
print sol.anagrams(['a'])
print sol.anagrams([''])
print sol.anagrams(['',''])
print sol.anagrams(['','a'])
print sol.anagrams(['','a', '','c'])
		        

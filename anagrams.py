class Solution:
  # @param {string[]} strs
  # @return {string[]}
  def anagrams(self, strs):
    from collections import defaultdict
    d = defaultdict(list)
    for s in strs:
      d[''.join(sorted(s))].append(s)
    
    ans = []
    for anagram in d.values():
      if len(anagram) < 2: continue
      ans.extend(anagram)
    return ans


sol = Solution()
# print sol.anagrams(['a','b','c'])
# print sol.anagrams(['a','c','c'])
# print sol.anagrams(['a'])
# print sol.anagrams([''])
# print sol.anagrams(['',''])
# print sol.anagrams(['','a'])
# print sol.anagrams(['','a', '','c'])
print sol.anagrams(["cab","abc","acb","duh","may","ill","buy","bar","","doc"])
		        

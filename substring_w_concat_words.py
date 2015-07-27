def findSubstring(s, words):
  
  if not words: return []

  N = len(s); n = len(words); k  = len(words[0])

  if N < n*k: return []

  dwords = {}
  for w in words:
    dwords[w] = 1 if not w in dwords else dwords[w] + 1

  outIndices = []; left = 0
  for j in range(k):
    left = j ;dsub = {}; count = 0
    for i in range(j, N - n*k + 1, k ):
      currw = s[i:i+k] 
      if currw in dwords:
	dsub[currw] = 1 if not currw in dsub else dsub[currw] + 1
	count += 1
	while dsub[currw] > dwords[currw]:
	  dsub[s[left:left+k]] -= 1
	  left += k 
	  count -= 1
	if count == n :
	  outIndices.extend([left])
      else: 
	left = i + k;  dsub = {};  count = 0

  return outIndices


s = "barfoothefoobarman"
words = ["foo", "bar"]
out = [0,9]
print out, "-", findSubstring(s, words)

s = "rman"
words = ["foo", "bar"]
out = [0,9]
print out, "-", findSubstring(s, words)

s = "barfoobarfoobarfoobarfoo"
words = ['bar','foo','bar']
out = [3,6,9]
print out, "-", findSubstring(s, words)

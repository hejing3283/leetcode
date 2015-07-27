def findSubstring(s, words):
  if not words: return []
  N = len(s); n = len(words); k  = len(words[0])
  # if N < n*k: return []
  dwords = {}
  for w in words:
    dwords[w] = 1 if not w in dwords else dwords[w] + 1

  outIndices = []; 
  for i in range(0, N - n*k +1 ) :
    ss = s[i:i+n*k]
    dsub = {}; j  = 0 
    while j < n:
      w = s[(i+k*j):(i+k*j + k)]
      if not w in dwords :
	break
      else:
	dsub[w] = 1 if not w in dsub else dsub[w] + 1
	if dsub[w] > dwords[w]:
	    break
      j += 1
    if j == n:
      outIndices.extend([i])
  return outIndices


s = "barfoothefoobarman"
words = ["foo", "bar"]
out = [0,9]
print "-", findSubstring(s, words)

s = "rman"
words = ["foo", "bar"]
print "-", findSubstring(s, words)

s ="barfoofoobarthefoobarman"
words = ['bar','foo','the']
out = [6,9,12]
print out, "-", findSubstring(s, words)

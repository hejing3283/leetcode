def findSubstring(s, words):
  
  if not words: return []

  N = len(s); n = len(words); k  = len(words[0])

  # if N < n*k: return []

  dwords = {}
  for w in words:
    dwords[w] = 1 if not w in dwords else dwords[w] + 1

  ### methods 1:
  outIndices = []; 
  for i in range(0, N - n*k +1 ) :
    ss = s[i:i+n*k]
    dsub = {}
    j  = 0 
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
 
  
  # ### methods 2

  # outIndices = []; left = 0
  # for j in range(k):
  #   left = j ;dsub = {}; count = 0
  #   for i in range(j, N - n*k + 1, k ):
  #     currw = s[i:i+k] 
  #     if currw in dwords:
	# dsub[currw] = 1 if not currw in dsub else dsub[currw] + 1
	# count += 1
	# while dsub[currw] > dwords[currw]:
	  # dsub[s[left:left+k]] -= 1
	  # left += k 
	  # count -= 1
	# if count == n :
	  # outIndices.extend([left])
  #     else: 
	# left = i + k;  dsub = {};  count = 0

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

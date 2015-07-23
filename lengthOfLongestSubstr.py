def lengthOfLongestSubstring(s):
  icand = 0; lenMax = 0;
  suniq = list( set(s) )
  keep = dict(zip(suniq,map(lambda x:-1, range(len(suniq))))) 
  for istr in range( len(s) ) : 
    if keep[s[istr]] >= icand:
      icand = keep[ s[istr]] + 1
    keep[s[istr]] = istr
    lenMax = max( lenMax, istr - icand + 1 )
  return lenMax
print 3, lengthOfLongestSubstring("abcabcbb")
print 1, lengthOfLongestSubstring("bbbbbb")
print 2, lengthOfLongestSubstring("aab")
print 2, lengthOfLongestSubstring("--x")

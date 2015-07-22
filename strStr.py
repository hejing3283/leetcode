def strStr( haystack, needle):
  '''
  brute force
  '''
  if (not haystack and not needle) or ( haystack and not needle)  :
    return 0
  elif ( not haystack and needle ) or (len(needle) > len(haystack):
    return -1
  else:
    ihs = 0 
    while ihs <  (len(haystack) - len(needle) + 1 ):
      ind = 0; k = ihs
      while ind <  len(needle):
        if haystack[k] == needle[ind]:
          ind += 1; k += 1
        else:
          break
      if ind == len(needle) :
        break 
      else:
        ihs += 1
    if ihs == (len(haystack) - len(needle) + 1): 
      return -1
    else:
      return ihs

print 3,strStr( 'xyx567x', '56')
print 0,strStr( 'xyx567x', '')
print -1,strStr( 'xyx567x', '0')
print 5,strStr( 'xyx567x', '7x')
print 0,strStr( 'xyx567x', 'xy')
print -1,strStr( '67x', 'xxxxy')
print -1,strStr( '', 'xxxxy')
print 0,strStr( '', '')
print 0,strStr( '1', '1')



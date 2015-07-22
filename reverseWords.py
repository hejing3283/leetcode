def reverseWords( s):
  ''' 
  insertion takes lot of time, can be improved
  '''
  snew = []; n = len(s) 
  _wd = []
  if not s.strip():
    return ""
  else:
    for ss in range(n):
      if s[ss] != " ": 
        _wd.append( s[ss])
      elif len(_wd) >0  :
        snew.insert(0,"".join(_wd) )
        snew.insert(0," " )
        _wd = []
      else:
	continue
    snew.insert(0, "".join(_wd ))
    return "".join(snew).strip()

print "-",reverseWords('the  sky is blue'),"-"
print "-",reverseWords('    '), "-"
print "-",reverseWords('  , '),"-"
print "-",reverseWords('   a   b '), "-"


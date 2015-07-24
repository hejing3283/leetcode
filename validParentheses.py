def isValid(s):
  if len(s) < 0 :
    return True
  if len(s) % 2 == 1:
    return False
  pd = {'(': ')', '[': ']', '{':'}' ,'<':'>'} 
  p2 = []
  i = 0
  while i < len(s) and s[i] :
    if s[i] in pd.keys():
      p2.insert(0, pd[ s[i] ])
    elif  len(p2) > 0 and s[i] != p2.pop(0):
      return False
    i += 1
  return len(p2) == 0 
print 'T', isValid( "()" )
print 'T', isValid( "()[]{}" )
print 'F', isValid( "([)]" )
print 'F', isValid( "(]" )
print 'T', isValid( "(())" )
print 'T', isValid( "[" )
print 'T', isValid( "[" )

def isValid(s):
  print 
  pd = {}
  i = 0
  ps = ['(', ')', '[', ']', '{', '}' ,'<', '>'] 
  while i < len(s) and s[i] :
    if s[i] in pd.keys():
      pd[ s[i]].append( i )
    else:
      pd[ s[i] ] = [i]
    i += 1
  print pd
  for p in range(0,len(ps),2):
    p1 = ps[p];  p2 = ps[p+1]
   
    if (p2 in pd.keys())  +  (p1 in pd.keys() )== 1:
      return False
    elif p2 in pd.keys() and p1 in pd.keys():
      v1 = pd[p1]; v2 = pd[p2]
      if len(v1) != len(v2) :
	return False
      for j in range(len(v2)) :
	if v1[j] >=  v2[ j ]:
	  return False

  return True 

print 'T', isValid( "()" )
print 'T', isValid( "()[]{}" )
print 'F', isValid( "([)]" )
print 'F', isValid( "(]" )

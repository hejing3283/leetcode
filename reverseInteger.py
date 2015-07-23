def reverse(x):
  if not isinstance( x, (int, long )):
    return 0 
  x = str(x)
  if len(x) == 1 and x.isdigit():
    return int(x)
  elif len(x) == 1 and not x.isdigit(): 
    return 0 
  else:
    x = x[::-1]
    sign = ''
    if not x[-1].isdigit():
      sign = x[-1] 
      x = x[:-1]

    i = 0 
    while i < len(x) -1:
      if x[i] == 0:
	x.pop(0)
	i += 1
      else:
	break
    out = int("".join([sign, x]) )
    if out > 214748364 or out < -214748364 :
      return 0
    else:
      return out  
  

print -321, reverse(-123)
print -1, reverse(-10000)
print 3, reverse(3)
print 0, reverse("")
print 0, reverse(10000000003)


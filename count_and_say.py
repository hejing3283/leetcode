# @param {integer} n
# @return {string}
def countAndSay(n):

  def count(s):
    # s is string representing a num
    count = 0; curr = '#'; t = ''
    for i in s:
      if i != curr:
	if curr != '#':
	  t += str(count) + curr
	curr = i
	count = 1
      else:
	count += 1
    t += str(count) + curr
    return t
  
  s = '1'
  for i in range(2, n+1):
    s = count(s)
  return s

print countAndSay(1)
print countAndSay(2)
print countAndSay(3)
print countAndSay(4)
print countAndSay(5)

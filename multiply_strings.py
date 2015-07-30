def multiply(n1, n2):
  # @param {string} num1
  # @param {string} num2
  # @return {string}
  n1 = n1[::-1] ;n2 = n2[::-1]
  ans = [] 
  carrier = [ 0 for _ in range(len(n1) + len(n2))]
  for i in range( len(n1) ):
    for j in range( len(n2) ):
      carrier[ i+j ]  += int(n1[i]) * int(n2[j]) 
  for i in range(len(carrier)):
    ans.insert(0, carrier[i] % 10 )
    if (i + 1) < len(carrier) :
      carrier[i+1] += carrier[i] / 10

  i = 0 
  while i < len(ans)-1 and ans[i] == 0 : i +=1
  ans = ans[i:]

  ans = [ str(i) for i in ans ]
  return ''.join(ans)

# print multiply('51','51')
# print multiply('7','2'), '14'
print multiply('100','0')
print multiply('0','0')
# print multiply('100',''), '0'
# print multiply('100000','100000')


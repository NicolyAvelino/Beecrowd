# Substituição em Vetor I
i = 0
while i < 10:
  N = int(input())
  if N != 0 and N > 0:
    print("X[%i] = %i" %(i,N))
  else:
    print("X[%i] = 1" %i)
  i +=1
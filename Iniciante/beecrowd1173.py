# Preenchimento de Vetor I
N = int(input())
V=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
  V[i] = N
  N = N*2
  print("N[%i] = %i"%(i, V[i]))
# Preenchimento de Vetor III
x = float(input())
for i in range(100):
  if i == 0:
    print("N[%i] = %.4f"%(i,x))
  else:
    print("N[%i] = %.4f"%(i,x/2))
    x = x/2
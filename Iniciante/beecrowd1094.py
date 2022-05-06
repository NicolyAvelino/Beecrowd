# Experiências
N = int(input())
C = 0
R = 0
S = 0
for i in range(0,N):
  Q, tipo = input().split()
  if tipo == "C":
    C += int(Q)
  elif tipo == "R":
    R += int(Q)
  elif tipo == "S":
    S += int(Q)
t = C + R + S
print("Total: %d cobaias"%t)
print("Total de coelhos: %d"%C)
print("Total de ratos: %d"%R)
print("Total de sapos: %d"%S)
print("Percentual de coelhos: %.2f %%"%((C*100)/t))
print("Percentual de ratos: %.2f %%"%((R*100)/t))
print("Percentual de sapos: %.2f %%"%((S*100)/t))
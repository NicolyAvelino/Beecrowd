# Maior e Posição
i = 1
p = 1
while i <= 100:
  N = int(input())
  if i == 1:
    m = N
  else:
    if N > m:
      m = N
      p = i
  i +=1
print(m)
print(p)
# Múltiplos de 13
x = int(input())
y = int(input())
soma = 0
if y<x:
  aux = x
  x = y
  y = aux
for num in range(x,y+1):
  if num%13 != 0:
    soma = soma + num
print(soma)
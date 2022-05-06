# Resto da Divisão
X = int(input())
Y = int(input())
if Y<X:
  aux = X
  X = Y
  Y = aux
for num in range(X+1,Y):
  if num%5==2 or num%5==3:
    print(num)
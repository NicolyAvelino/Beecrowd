# Soma de Impares Consecutivos I
x = int(input())
y = int(input())
soma = 0
for num in range(y+1,x):
  if num%2 !=0:
    soma = soma + num
print(soma)
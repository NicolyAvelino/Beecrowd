# Soma de Ímpares Consecutivos II
N = int(input())
for i in range(N):
  linha = [int (num) for num in input().split()]
  x = min(linha)
  y = max(linha)
  soma = 0
  for num in range(x+1,y):
    if num%2!=0:
      soma = soma + num
  print(soma)
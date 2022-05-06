# Idades
x = int(0)
i = 0
soma = 0
while x >= 0:
  num = int(input())
  if num >= 0:
    soma += num
    i += 1
  else:
    break
m = soma / i
print("%.2f"%m)
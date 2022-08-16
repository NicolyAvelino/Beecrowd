# Positivos e Média
i = 0
pos = 0
soma = 0
while i <= 5:
  N = float(input())
  if N > 0:
    pos +=1 
    soma += N
  i +=1
div = soma / pos
print("%i valores positivos" %pos)
print("%.1f"%(div))
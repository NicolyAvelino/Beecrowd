# Pares, Ímpares, Positivos e Negativos
i = 0
par = 0
imp = 0
pos = 0
neg = 0
while i < 5:
  N = int(input())
  if N%2 == 0:
    par +=1 
  if N%2 == 1:
    imp +=1
  if N > 0:
    pos +=1 
  if N < 0:
    neg +=1
  i += 1
print("%i valor(es) par(es)"%par)
print("%i valor(es) impar(es)"%imp)
print("%i valor(es) positivo(s)"%pos)
print("%i valor(es) negativo(s)"%neg)
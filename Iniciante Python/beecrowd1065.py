# Pares entre Cinco Números
i = 0
par = 0
while i < 5:
  N = int(input())
  if N%2 == 0:
    par +=1 
  i +=1
print("%i valores pares" %par)
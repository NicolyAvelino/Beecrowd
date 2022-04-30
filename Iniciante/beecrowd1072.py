# Intervalo 2
N = int(input())
i = 0
dentro = 0
fora = 0
while i < N:
  X = int(input())
  if X >=10 and X <=20:
    dentro += 1
  else:
    fora += 1
  i += 1
print("%i in" %dentro)
print("%i out" %fora)
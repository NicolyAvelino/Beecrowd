# Tipo de Combustível
a = 0
g = 0
d = 0
while True:
  n = int(input())
  if n == 1:
    a += 1
  if n == 2:
    g += 1
  if n == 3:
    d += 1
  if n == 4:
    break
print("MUITO OBRIGADO")
print("Alcool: %i"%a)
print("Gasolina: %i"%g)
print("Diesel: %i"%d)
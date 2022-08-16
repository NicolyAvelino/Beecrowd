# Validação de Nota
i = 0
num = 0
while i < 2:
  nota = float(input())
  if nota > 0 and nota <= 10:
    num += nota
    i += 1
  else:
    print("nota invalida")
m = num / 2
print("media = %.2f"%m)
# Média 3
n1,n2,n3,n4 = map(float, input().split())
mP = (n1 * 2 + n2 *3 + n3 *4 + n4 *1) / 10
print("Media: %.1f" %mP)
if mP >= 7.0:
  print("Aluno aprovado.")
elif mP < 5.0:
    print("Aluno reprovado.")
elif mP >= 5.0 and mP <= 6.9:
  print("Aluno em exame.")
  n5 = float(input())
  print("Nota do exame: %.1f" %n5)
  nE = (n5 + mP)/2
  if nE >= 5.0:
    print("Aluno aprovado.")
    print("Media final: %.1f"%nE)
  else:
    print("Aluno reprovado.")
    print("Media final: %.1f"%nE)
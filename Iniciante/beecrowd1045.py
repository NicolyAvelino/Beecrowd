# Tipos de Triângulos
A,B,C = map(float, input().split())
list = [A,B,C]
list.sort(reverse = True)
A = list[0]
B = list[1]
C = list[2]
if (A < B+C):
  if (A**2 == B**2 + C**2):
    print("TRIANGULO RETANGULO")
  elif (A**2 > B**2 + C**2):
    print("TRIANGULO OBTUSANGULO")
  else:
    print("TRIANGULO ACUTANGULO")
  if (A == B and B == C):
    print("TRIANGULO EQUILATERO")
  elif (A==B or B==C):
    print("TRIANGULO ISOSCELES")
else:
  print("NAO FORMA TRIANGULO")
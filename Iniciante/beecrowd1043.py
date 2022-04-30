# Triângulo
A,B,C = map(float, input().split())
if (A+B > C) and (B+C > A) and (A+C > B):
  p = A + B + C
  print("Perimetro = %.1f"%p)
else:
  area = (A + B) * C / 2
  print("Area = %.1f"%area) 
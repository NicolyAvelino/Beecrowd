# Fórmula de Bhaskara
A, B, C = map(float, input().split())
delta = B ** 2 - 4 * A * C
if A == 0.0 or delta < 0:
  print("Impossivel calcular")
else:
  print("R1 = %.5f"%((-B + pow(delta, 1/2)) / (2 * A)))
  print("R2 = %.5f"%((-B - pow(delta, 1/2)) / (2 * A)))
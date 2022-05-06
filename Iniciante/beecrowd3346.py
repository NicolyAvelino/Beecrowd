# Flutuação do PIB
f1, f2 = map(float, input().split())
PIB = ((((1.0 + f1/100.00) * (1.0 + f2/100.00)) - 1.0) * 100.0)
print("%.6f"%PIB)
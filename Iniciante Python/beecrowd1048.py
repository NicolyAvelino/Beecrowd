# Aumento de Salário
N = float(input())
if N >= 0 and N <=400.00:
  reaj = N * 0.15
  sal = N + reaj
  p =  15
elif N >= 400.01 and N <= 800.00:
  reaj = N * 0.12
  sal = N + reaj
  p = 12
elif N >= 800.01 and N <= 1200.00:
  reaj = N * 0.1
  sal = N + reaj
  p = 10
elif N >= 1200.01 and N <= 2000.00:
  reaj = N * 0.07
  sal = N + reaj
  p = 7
else:
  reaj = N * 0.04
  sal = N + reaj
  p = 4
print("Novo salario: %.2f"%sal)
print("Reajuste ganho: %.2f"%reaj)
print("Em percentual: %.f %%"%p)
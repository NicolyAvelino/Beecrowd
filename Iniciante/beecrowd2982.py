# A Greve para ou Continua?
n = int(input())
g = 0
v = 0
for i in range(n):
  t,c = input().split()
  t = str(t)
  c = int(c)
  if t == "G":
    v += c
  else:
    g += c
if v > g:
  print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
  print("A greve vai parar.")
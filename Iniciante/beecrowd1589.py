# Bob Conduite
t = int(input())
soma = 0
for i in range(t):
  r1,r2 = map(int, input().split())
  soma = r1 + r2
  print(soma)
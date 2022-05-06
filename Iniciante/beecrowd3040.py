# A Árvore de Natal
N = int(input())
for i in range(N):
  a,d,g = map(int, input().split())
  if a>=200 and a<=300 and d>=50 and g>=150:
    print("Sim")
  else:
    print("Nao") 
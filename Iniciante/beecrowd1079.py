# Médias Ponderadas
N = int(input())
c = 1
while c <= N:
  n1,n2,n3 = map(float, input().split())
  mediaP = (n1*2 + n2 * 3 + n3 * 5)/ 10
  print("%.1f" %mediaP)
  c += 1
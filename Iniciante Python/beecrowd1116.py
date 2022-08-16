#  Dividindo X por Y
N = int(input())
for i in range(N):
  n1, n2 = map(int, input().split())
  if n2 != 0:
    div = n1 / n2
    print("%.1f" %div)
  else:
    print("divisao impossivel")
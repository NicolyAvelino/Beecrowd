# Prefácio
a,b = map(int, input().split())
r = a%b
if r <0:
  r = r - b
  q = int((a-r)/b)
else:
  q = int((a-r)/b)
print("%i %i"%(q,r))
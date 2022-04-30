# O Maior
A, B, C = map(int, input().split())
mAB = (A + B + abs(A - B))/2
res = (mAB + C + abs(mAB - C))/2
print("%i eh o maior" %res)
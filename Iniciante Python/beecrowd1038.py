# Lanche
c, item = map(int, input().split())
if c == 1:
  preco = 4.00
elif c == 2:
  preco = 4.50
elif c == 3:
  preco = 5.00
elif c == 4:
  preco = 2.00
else:
  preco = 1.50
t = item * preco
print("Total: R$ %.2f" %t)
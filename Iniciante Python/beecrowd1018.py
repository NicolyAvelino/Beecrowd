# Cédulas
valor = int(input())
print(valor)
n100 = valor // 100
valor %= 100
n50 = valor // 50
valor %= 50
n20 = valor // 20
valor %= 20
n10 = valor // 10
valor %= 10
n5 = valor // 5
valor %= 5
n2 = valor // 2
valor %= 2
print("%i nota(s) de R$ 100,00" %n100)
print("%i nota(s) de R$ 50,00" %n50)
print("%i nota(s) de R$ 20,00" %n20)
print("%i nota(s) de R$ 10,00" %n10)
print("%i nota(s) de R$ 5,00" %n5)
print("%i nota(s) de R$ 2,00" %n2)
print("%i nota(s) de R$ 1,00" %valor)
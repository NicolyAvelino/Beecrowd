# Idade em Dias
id = int(input())
A = id // 365
id %= 365
B = id // 30
id %= 30
C = id // 1
id %= 1
print("%i ano(s)" %A)
print("%i mes(es)" %B)
print("%i dia(s)" %C)
# Sequência de Números e Soma
while True:
    soma = 0
    num = []
    m,n = map(int, input().split())
    if (m <= 0) or (n <=0):
        break
    if  m > n:
        aux = m
        m = n
        n = aux
    for i in range(m,n+1):
        num.append(i)
        soma = sum(num)
        if i == n:
            print(i,"Sum=%i"%soma)
        else:
            print(i,end=" ")
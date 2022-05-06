# Preenchimento de Vetor II
T = int(input())
vet = []
for i in range(1000):
    for con in range(0,T):
        vet.append(con)
    print("N[%d] = %d"%(i,vet[i]))
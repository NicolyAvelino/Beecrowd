# Número Primo
N = int(input())
for i in range(N): 
    X=int(input())
    soma = 0
    for i in range(1,X):
        if X%i == 0:
          soma+=i
    if soma >2:
      print("%i nao eh primo"%X) 
    else:
      print("%i eh primo"%X)
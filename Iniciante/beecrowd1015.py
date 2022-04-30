# Distância Entre Dois Pontos
x1,y1 = map(float, input().split())
x2,y2 = map(float, input().split())
soma = pow((x2 - x1),2) + pow((y2 - y1),2)
raiz = pow(soma,1/2)
print("%.4f" % raiz)
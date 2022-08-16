# Área
A,B,C = input().split(" ")
TRIANG = (float(A) * float(C))/2
CIR =  3.14159 * pow(float(C),2)
TRAP = ((float(A) + float(B)) * float(C) )/2
QUAD = pow(float(B),2)
RET = float(A) * float(B)
print("TRIANGULO: %.3f" % TRIANG)
print("CIRCULO: %.3f" % CIR)
print("TRAPEZIO: %.3f" % TRAP)
print("QUADRADO: %.3f" % QUAD)
print("RETANGULO: %.3f" % RET)
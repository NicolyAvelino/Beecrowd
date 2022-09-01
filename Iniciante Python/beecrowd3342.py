# Keanu
n = int(input())
div = (n*n)/2
if n%2 == 0:
    print("%i casas brancas e %i casas pretas"%(div,div))
else:
    print("%i casas brancas e %i casas pretas"%(div+1,div))
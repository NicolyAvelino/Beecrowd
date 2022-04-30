# Tempo de Jogo
hI,hF = map(int, input().split())
if hI > hF:
  t = (24 - hI) + hF
  print("O JOGO DUROU %d HORA(S)"%t)
if hF > hI:
  t = hF - hI
  print("O JOGO DUROU %d HORA(S)"%t)
if hI == hF:
  t = 24
  print("O JOGO DUROU %d HORA(S)"%t)
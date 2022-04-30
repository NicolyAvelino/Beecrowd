# Notas e Moedas
v = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05,0.01]
print("NOTAS:")
for nota in notas:
  quant_nota = int(v / nota)
  print("{} nota(s) de R$ {:.2f}".format(quant_nota, nota))
  v -= quant_nota * nota
print("MOEDAS:")
for moeda in moedas:
  quant_moeda = int(round(v,2) / moeda)
  print("{} moeda(s) de R$ {:.2f}".format(quant_moeda, moeda))
  v -= quant_moeda * moeda
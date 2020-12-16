value = []
for i in range(0, 5,1):
   print(i + 1)
   entrada = float(input('digite a  Sua nota, do Enem de acordo com o numero inciar: '))
   value.append(entrada)


print((value[0] + value[1] + value[2] + value[3] + value[4]) / 5)

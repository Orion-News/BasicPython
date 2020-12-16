n = int(input('Digite um numero para descubrir a Sequencia fibonacci dele: _while '))
v = 1
i = 2
con = 1
while (con < (n + 1)):
    print(v)
    v=v+i
    i=i+1
    con=con+1

n = int(input("Digite um numero para descubrir a Sequencia fibonacci dele: -For- s "))
v = 1
i = 2
for con in range(1, (n + 1), 1):
    print(v)
    v=v+i
    i=i+1

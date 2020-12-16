n = int(input('Digite um numero inteiro para saber se é primo: '))
qtd = 0
d = 1
while (d <= n):
    if n % d ==0:
        qtd += 1
    d += 1
if qtd==2:
    print('é primo')
else:
    print('não é primo')

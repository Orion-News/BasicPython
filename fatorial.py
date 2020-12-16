def fatorial(n):
    fat=1
    con=1
    while (con< (n+1)):
        fat=fat*con
        con=con+1
    print(fat)

k=int(input('digite um número para saber seu fatorial: '))
fatorial(k)
        

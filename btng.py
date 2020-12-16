import random

def Entrada():
    n = int(input('Digite um numero entre 0 e 6: '))
    return n

def Embarcacao():
    lis = [0] * 3
    lis[0] = random.randint(0,6)
    lis[1]= lis[0] + 1
    lis[2] = lis[1] + 1
    return lis

def Coordenadas(p, e):
    a = 0
    if(p == e[0] or p == e[1] or p == e[2]):
        a = a + 1
        v = 'o valor de acertos! é : %d' % a
        print(v.upper())
        return a
    return a

def Estatistica(a, t):
    print('você encontrou as coordernadas do navio! Parabéns!'.upper())
    p = a/t
    v = 'parabens você ganhou!, a quantidade de tentativas é %d você teve um percentual de acertos no valor de %.2f porcento' % (t, p)
    print(v.upper())

def Execucao():
    afundado = False
    t = 0
    a = 0
    e = Embarcacao()
    while afundado == False:
        p = Entrada()
        if(p < 0 or p > 6):
            s = 'valor invalido, o número %d não esta entre 0 e 6!' % p
            print(s.upper())
            t += 1
        else: 
            t += 1
            a += Coordenadas(p, e)
            if a == 3:
                Estatistica(a,t)
                afundado = True
Execucao()
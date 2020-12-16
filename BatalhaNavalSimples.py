import random

"""
definir uma sequencia de 3 numeros inteiros aleatorios, entre 0 e 6;
difinir quantidade de tentativas, para exibir o valor da porcetagem de acerto, entre 0 e 1 que seja um valor flutuante;
definir quantidades de acertos, para usar como step de fim de jogo... caso seja igual aos 3 numeros sequencias aleatorios;
definir variavel falha
enquanto falha for igual a False:
pedir entrada do usuarios;
Verificar se a entrada do usuario esta entre os 3 numeros inteiros definidos sequencias,
se estiver validar entre os 3 numeros sequencias definido...
se a entrada do usuario for igual a um dos 3 numeros sequencias pedidos, acrescentar acertos com + 1;
se acertos for igual a 3, definir falha como True, exibir a quantidade de tentativas e exibir a porcentagem de tentativas dividido pelo a quantidades de numeros sequencias definidos;
"""

barcoParte1Local = random.randint(0,6)
barcoParte2Local = barcoParte1Local + 1
barcoParte3Local = barcoParte2Local + 1
tentativas = 0
acertos = 0
wasFalied = False
while (wasFalied == False):
    palpite = int(input('digite um numero entre 0 a 6: '))
    if(palpite < 0 or palpite > 6):
        print('valor invalido, não esta entre 0 e 6, digite um numero entre 0 e 6: ')
    else:
        tentativas = tentativas + 1
        print(tentativas)
        if(palpite == barcoParte3Local or palpite == barcoParte2Local or palpite == barcoParte1Local):
            acertos = acertos + 1
            print('o valor de acertos! é : ', acertos)
            if(acertos == 3):
                print(acertos)
                wasFalied = True
                print('você afundou o navio, chupa essa poha!')
print('parabens você ganhou!, a quantidade de tentativas, ', tentativas, 'você teve uma divisão de: ', (acertos/tentativas), 'porcento!')

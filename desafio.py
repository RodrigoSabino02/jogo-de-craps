 import random 

 dado = random.randint(2, 12)
 pontos = 0

if(dado == 7 or dado == 11):
    print('voce tirou um {} e ganhou'.format(dado))
    print('voce fez {} pontos'.format(pontos))
elif(dado == 2 or dado == 3 or dado == 12):
    print('voce tirou um {} e perdeu'.format(dado))
    print('voce fez {} pontos'.format(pontos))
else:
    while 1:
        print('voce tirou um {}'.format(dado))
        dado = random.randint(2, 12)
        pontos += 1
        print('voce ganhou um ponto, sua quantidade de pontos e {}'.format(pontos))
        if(dado == 7):
            print('voce tirou um 7 e perdeu')
            print('voce fez {} pontos!'.format(pontos))
            break


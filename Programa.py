from random import randint
computador = randint(0, 5) # faz o computador 
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}!'.format(computador, jogador))    

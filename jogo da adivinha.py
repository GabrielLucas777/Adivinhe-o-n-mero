import random
from time import sleep
print('\t JOGO DA ADIVINHA')
input('Pressione enter para continuar...')
print('iniciando...')
sleep(2)

numero_gerado = random.randint(1,100)
print("Um número foi gerado!")
while True:
    numero = int(input("Digite o número que acha que foi gerado: "))
    
    if numero_gerado > numero:
        print('Chute um número MAIOR')
    elif numero_gerado < numero:
        print('chute um número MENOR')
    else:
        print(f'Parabéns, Você acertou. O número gerado foi o {numero_gerado}')
        print('Deseja continuar?')
        resp = input('Pressione S ou N: ')
        if resp == 'n':
            print('encerrando em 3,2,1...')
            break



        
    
    

        
    

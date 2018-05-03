import random
import keyboard
import os

sorteados = []

def numeros_sorteados(sorteados):
    print('\n=================')
    print("NUMEROS QUE JA FORAM SORTEADOS: \n")
    print(sorteados)
    print('=================\n')


while True:
    if not keyboard.is_pressed('esc'):
        opcao = int(input("1) DIGITAR NUMERO TOTAL DE PARTICIPANTES\n2) SORTEAR UM NUMERO\n3) Sair \n\n"))
        os.system('clear')
        if opcao == 1:
            participantes = int(input("\nQuantas participantes? "))
            os.system('clear')
        if opcao == 2:
            try:
                participantes
                numero = random.randint(0,participantes)
                if not numero in sorteados:
                    sorteados.append(numero)
                    numeros_sorteados(sorteados)
                    print("\n NUMERO SORTEADO: "+str(numero)+"\n\n")
                else:
                    numeros_sorteados(sorteados)
                    if (len(sorteados) - 1) == participantes:
                        os.system("clear")
                        print("\n\n Acabou sorteio!! \n\n")
                        break
                    else:
                        print("\n Sorteie outro numero! \n\n")

            except NameError:
                print("\nDigite o TOTAL DE PARTICIPANTES primeiro\n\n")
        if opcao == 3:
            break
    else:
        break
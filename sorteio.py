from random import randint
import keyboard
import os

lista_sorteados = []

def sorteio(total):
    sorteado = randint(1, total)
    while sorteado in lista_sorteados:
        sorteado = randint(1, total)
    lista_sorteados.append(sorteado)
    if len(lista_sorteados) == total:
        print('Acabou o sorteio!')
    return sorteado

def numeros_sorteados(lista_sorteados):
    print('\n=================')
    print("NUMEROS QUE JA FORAM SORTEADOS: \n")
    #lista_sorteados.sort()
    print(lista_sorteados)
    print('=================\n')
    print('Total de números sorteados: ', len(lista_sorteados))
    print('=================\n')

participantes = int(input("\nQuantas participantes? "))

while True:
    if not keyboard.is_pressed('esc'):
        opcao = int(input("1) ALTERAR NUMERO TOTAL DE PARTICIPANTES\n2) SORTEAR UM NUMERO\n3) Sair \n\n"))
        os.system('clear')
        if opcao == 1:
            participantes = int(input("\nQuantas participantes? "))
            os.system('clear')
        if opcao == 2:
            try:
                print('NÚMERO SORTEADO: ', sorteio(participantes))
                numeros_sorteados(lista_sorteados)
            except NameError:
                print("\nDigite o TOTAL DE PARTICIPANTES primeiro\n\n")
        if opcao == 3:
            break
    else:
        break

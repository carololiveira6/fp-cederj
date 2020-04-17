'''
Utilizando subprogramação, faça um programa que leia da entrada padrão uma linha podendo conter vários números de ponto flutuante. Caso exista, escreva qual o número que mais ocorreu e a quantidade de vezes que ocorreu. Caso haja empate escreva um deles. Caso a linha lida seja uma string vazia, escreva a mensagem: “nenhum número foi lido!!!”
'''

# Subprogramas
def mostrar(numero):
    lista = []
    qntNum = 0
    numRep = None
    if len(numero) == '':
        print('Nenhum número foi lido!!!')
    else:
        for i in range(len(numero)):
            lista.append(float(numero[i]))
        for j in range(len(lista)):
            x = lista.count(lista[j])
            if x > qntNum:
                 numRep = lista[j]
                 qntNum = lista.count(numRep)
    print('Valor que mais ocorreu: {} que foi encontrado {} vez(es)'.format(numRep, qntNum))


# Programa Principal

num = input().split()
mostrar(num)





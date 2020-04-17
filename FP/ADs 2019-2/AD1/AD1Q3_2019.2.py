'''
Utilizando subprogramação, faça um programa que leia da entrada padrão, em uma única string, dois números inteiros separados por um espaço em branco, representando as duas dimensões de uma matriz bidimensional. Construa uma matriz bidimensional com as dimensões lidas e com valores gerados aleatoriamente, via função randint importada do módulo random, no intervalo 100 a 999.
Escreva:
(1) O conteúdo da matriz, onde cada linha a ser escrita possua apenas números inteiros, sem vírgulas nem colchetes;
(2) A posição (linha, coluna) do maior valor sorteado e o seu respectivo valor;
(3) A soma de cada linha, de todas as linhas da matriz;
(4) A soma de cada coluna, de todas as colunas da matriz.
'''

#Subprogramas
def gerarM(numL, numC, min, max):
    from random import randint
    valores = [None] * numL
    for i in range(numL):
        valores[i] = [0] * numC
        for j in range(numC):
            valores[i][j] = randint(min, max)
    return valores

def mostrarM(vals, minL, maxL, minC, maxC):
    for i in range(minL, maxL):
        for j in range(minC, maxC):
            print(vals[i][j], end=" ")
        print()
    print()
    return None

def somatorio(valores, linha, coluna):
    for numLinha in range(linha):
        totalLin = 0
        for numColuna in range(coluna):
            totalLin += valores[numLinha][numColuna]
        print(f'Soma da Linha {numLinha} = {totalLin}')
    print()

    for numColuna in range(coluna):
        totalCol = 0
        for numLinha in range(linha):
            totalCol += valores[numLinha][numColuna]
        print(f'Soma da Coluna {numColuna} = {totalCol}')
    print('\n')

    return None

def posicaoMaior(valores):
    posMaior = (0, 0)
    valorMaior = valores[0][0]
    for i in range(len(valores)):
        for j in range(len(valores[i])):
            if valores[i][j] > valorMaior:
                valorMaior = valores[i][j]
                posMaior = (i, j)
    print(f'Posição do Maior: {posMaior} Maior Valor: {valorMaior}')
    print()
    return None

# Programa Principal
num = input().split()
numL = int(num[0])
numC = int(num[1])
vals = gerarM(numL, numC, 100, 999)
mostrarM(vals, 0, numL, 0, numC)
posicaoMaior(vals)
somatorio(vals,numL,numC)

'''Faça um programa que peça ao usuário as dimensões de uma matriz bidimensional, chamada de valores, de números inteiros a ser gerada em aleatoriamente no intervalo 10 a 99. Via subprogramação:
• Mostre a matriz gerada;
• Ordene as linhas da matriz em ordem crescente da soma de seus valores;
• Mostre a matriz ordenada.
Nesse programa, seu programa DEVE implementar e utilizar o método da partição.
Entrada
A entrada é composta por uma primeira linha, que define a quantidade L de linhas e a quantidade C de colunas da matriz a ser gerada.
Saída
L linhas, onde cada linha possui C valores inteiros no intervalo 10 a 99 que correspondem à matriz original sorteada; seguida(s) de uma linha em branco; e por L linhas, onde cada linha possui C valores que correspondem à matriz ordenada.
'''

from typing import List
from random import randint

# Subprogramas


def gerarM(m: int, n: int):
    matriz = [[randint(10, 100) for i in range(m)] for j in range(n)]
    return matriz

def mostrarM(matriz: List[List[int]]):
    for linha in matriz:
        print(*linha)
    return None

def ordenarSoma(matriz: List[List[int]]):
    somaLinha = []
    for u, linha in enumerate(matriz):
        soma = (sum(linha), u, linha)
        somaLinha.append(soma)
    linhasOrdenadas = []
    for i, j, linha in sorted(somaLinha):
        linhasOrdenadas.append(linha)
    return linhasOrdenadas

def ordenarM(matriz: List[List[int]]) -> List[List[int]]:
    tamanho = len(matrizOrdenada)
    if tamanho <= 1:
        return matrizOrdenada
    centro = tamanho // 2
    pivo = matrizOrdenada[centro]
    menoresIguais = []
    maiores = []
    elemsEsquerda = matrizOrdenada[:centro]
    elemsDireita = matrizOrdenada[centro + 1:]
    for x in elemsEsquerda + elemsDireita:
        if x <= pivo:
            menoresIguais.append(x)
        else:
            maiores.append(x)
    return sorted(menoresIguais) + [pivo] + sorted(maiores)


# Programa Principal

entrada = input()
n, m = entrada.split()
n = int(n)
m = int(m)
vals = gerarM(n, m)
mostrarM(vals)
print()
mostrarM(ordenarSoma(vals))


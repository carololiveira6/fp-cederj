'''
Considere a existência de uma linha vertical que representa o intervalo [0, 2n]. Agora desenhe traços verticais apoiados nos pontos 1, 2, 3, ... 2n-1 da linha vertical imaginária. O traço vertical no ponto médio do intervalo deve ter altura n, os traços nos pontos médios dos subintervalos esquerdo e direito têm altura n-1, e assim por diante. Diremos que isso é uma régua de ordem n no intervalo [0, 2n].
Dado o valor de n, escreva um programa recursivo que escreva tal régua na saída padrão.
Entrada
A entrada é composta por um único valor n inteiro não negativo.
Saída
A régua impressa da saída padrão com o formato conforme apresentado no exemplo
'''

# Subprogramas

def linhaVertical(x: int):
    inicio = 1
    fim = 2 ** x
    escrevaRegua(fim, inicio, x)
    return None


def escrevaRegua(fim, inicio, x):
    if x == 0:
        return
    fim -= 1
    pMedio = (fim + inicio) // 2
    escrevaRegua(pMedio, inicio, x - 1)
    print(f'{pMedio:02} ' + '-' * x)
    escrevaRegua(fim + 1, pMedio + 1, x - 1)


# Programa Principal

x = int(input())
linhaVertical(x)
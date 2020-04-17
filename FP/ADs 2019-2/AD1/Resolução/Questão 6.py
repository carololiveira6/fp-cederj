from random import randint                                                               # Importa o comando randint de random
from typing import List                                                                  # Importa o comando list de typing

# Subprogramas

def construir_matriz(n: int, m: int):
    matriz = [[randint(10, 100) for _ in range(m)] for _ in range(n)]
    return matriz



def imprimir_matriz(matriz: List[List[int]]):
    for linha in matriz:
        print(*linha)
    return None


def orderna_por_soma_das_linha(matriz: List[List[int]]) -> List[List[int]]:
    soma_da_linha = []
    for i, linha in enumerate(matriz):
        dados = (sum(linha), i, linha)
        soma_da_linha.append(dados)
    linhas_ordenadas = []
    for _, _, linha in ordenar(soma_da_linha):
        linhas_ordenadas.append(linha)
    return linhas_ordenadas


def ordenar(lista):
    tamanho = len(lista)
    if tamanho <= 1:
        return lista
    central = tamanho // 2
    pivo = lista[central]
    menores_ou_iguais_ao_pivo = []
    maiores_que_o_pivo = []
    elementos_a_esquerda_do_pivo = lista[:central]
    elementos_a_direita_do_pivo = lista[central + 1:]
    for n in elementos_a_esquerda_do_pivo + elementos_a_direita_do_pivo:
        if n <= pivo:
            menores_ou_iguais_ao_pivo.append(n)
        else:
            maiores_que_o_pivo.append(n)
    return ordenar(menores_ou_iguais_ao_pivo) + [pivo] + ordenar(maiores_que_o_pivo)


# Programa Principal

entrada = input()
n, m = entrada.split()
n = int(n)
m = int(m)

valores = construir_matriz(n, m)
imprimir_matriz(valores)
print()
imprimir_matriz(orderna_por_soma_das_linha(valores))


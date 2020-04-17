# Subprogramas

def linha_vertical(n: int):
    inicio = 1
    final = 2 ** n
    escrever_regua(final, inicio, n)
    return None


def escrever_regua(final, inicio, n):
    if n == 0:
        return
    final -= 1
    ponto_medio = (final + inicio) // 2
    escrever_regua(ponto_medio, inicio, n - 1)
    print(f'{ponto_medio:02} ' + '-' * n)
    escrever_regua(final+1, ponto_medio+1, n - 1)


# Programa Principal

n = int(input())
linha_vertical(n)


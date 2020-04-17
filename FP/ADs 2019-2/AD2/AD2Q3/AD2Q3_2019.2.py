from math import inf

arquivoEntrada = 'arquivo_entrada.txt'
centroide = (0, 0)
with open(arquivoEntrada, 'r', encoding='utf8') as arquivo:
    somaX = 0
    somaY = 0
    count = 0
    for pontosPorLinha in arquivo:
        pontosPorLinha = pontosPorLinha.strip()
        x, y = pontosPorLinha.split()
        x = float(x)
        y = float(y)
        somaX += x
        somaY += y
        count += 1
    centroide = (somaX / count, somaY / count)
    print(f'Centroide: ({centroide[0]:.1f}, {centroide[1]:.1f})')

with open(arquivoEntrada, 'r', encoding='utf8') as arquivo:
    menorDistancia = inf
    centroideX, centroideY = centroide
    pontoMaisProximo = centroide
    for pontosPorLinha in arquivo:
        pontosPorLinha = pontosPorLinha.strip()
        x, y = pontosPorLinha.split()
        x = float(x)
        y = float(y)
        distanciaEntreDoisPontos = ((x - centroideX) ** 2 + (y - centroideY) ** 2) ** (1 / 2)
        if distanciaEntreDoisPontos < menorDistancia:
            menorDistancia = distanciaEntreDoisPontos
            pontoMaisProximo = (x, y)

    print(f'Ponto Mais Próximo: ({pontoMaisProximo[0]:.1f}, {pontoMaisProximo[1]:.1f})')

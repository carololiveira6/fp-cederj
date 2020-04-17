import os

nomeDoArquivo = 'teste.txt'

def insereOrdenado(nomeDoArquivo: str, novoValor: float):
    nomeArquivoTemp = 'temporario.txt'
    arquivoEntrada = open(nomeDoArquivo, 'r', encoding='utf8')
    arquivoTemporario = open(nomeArquivoTemp, 'w', encoding='utf8')
    valorInserido = False
    with arquivoEntrada as entrada, arquivoTemporario as saida:
        for linha in entrada:
            valor = linha.strip()
            if not valorInserido and valor != '':
                valor = float(valor)
                if novoValor < valor:
                    saida.write(f'{novoValor}\n')
                    valorInserido = True
                saida.write(linha)
            else:
                saida.write(linha)
        if not valorInserido:
            saida.write(f'{novoValor}\n')
    os.remove(nomeDoArquivo)
    os.rename(nomeArquivoTemp, nomeDoArquivo)


if __name__ == '__main__':
    insereOrdenado(nomeDoArquivo, 6.0)

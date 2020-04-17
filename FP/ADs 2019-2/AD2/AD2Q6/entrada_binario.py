import struct

arquivoEntrada = open('entrada.txt', 'r', encoding='utf8')
arquivoSaida = open('valores.bin', 'wb')
with arquivoEntrada as entrada, arquivoSaida as saida:
    for linha in entrada:
        linha = linha.strip()
        numInteiros = [int(n) for n in linha.split()]
        for inteiro in numInteiros:
            saida.write(struct.pack('i', inteiro))

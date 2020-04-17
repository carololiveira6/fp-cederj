import struct

arquivoEntrada = open('arquivoentrada.txt', 'r', encoding='utf8')
arquivoSaida = open('entrada.bin', 'wb')
with arquivoEntrada as entrada, arquivoSaida as saida:
    for linha in entrada:
        linha = linha.strip()
        inteiro = [int(n) for n in linha.split()]
        for numero in inteiro:
            saida.write(struct.pack('i', numero))

import struct

arquivoEntrada = 'entrada.bin'
arquivoSaida = 'saida.bin'
arqEntrada = open(arquivoEntrada, 'rb')
arqSaida = open(arquivoSaida, 'wb')


def inteiro(quatroBytes):
    return struct.unpack('i', quatroBytes)[0]


with arqEntrada as entrada, arqSaida as saida:
    clientesQ = inteiro(arqEntrada.read(4))
    print(f'Quantidade de clientes visitados na última semana: Q = {clientesQ}')
    clientesE = inteiro(arqEntrada.read(4))
    print(f'Quantidade de clientes visitados no último dia: E = {clientesE}')
    clienteSi = set()
    for _ in range(clientesE):
        clienteSi.add(inteiro(arqEntrada.read(4)))
    print(f'Os clientes visitados no último dia são: {clienteSi}')
    for _ in range(clientesQ):
        cliente = inteiro(arqEntrada.read(4))
        flagSaida = 0 if cliente in clienteSi else 1
        arqSaida.write(struct.pack('i', flagSaida))

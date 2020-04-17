import struct

arquivoBin = 'valores.bin'
arquivoEntrada = open(arquivoBin, 'rb')

def int(quatroBytes):
    return struct.unpack('i', quatroBytes)[0]

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

with arquivoEntrada as entrada:
    qntPares = int(arquivoEntrada.read(4))
    for _ in range(qntPares):
        a = int(arquivoEntrada.read(4))
        b = int(arquivoEntrada.read(4))
        print(mdc(a, b))

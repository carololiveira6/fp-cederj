# Subprogramas

def converter_base_2_para_10(n:str) -> int:
    n_reverso = reversed(n)
    num_base_10 = 0
    for i, numero in enumerate(n_reverso):
        numero = int(numero)
        num_base_10 += numero * (2 ** i)
    return num_base_10


def converter_para_bases(n_base_10:int, base:int):
    algarismos_reversos = []
    divisor = n_base_10
    while True:
        divisor, resto = divmod(divisor, base)
        algarismos_reversos.append(str(resto))
        if divisor == 0:
            break
    return ''.join(reversed(algarismos_reversos))


def converte(binario: str, base: int):
    return converter_para_bases(converter_base_2_para_10(binario), base)


def converte_base_3_a_10(binario):
    valores = []
    for base in range(3, 11):
        valores.append(converte(binario, base))
    return valores


# Programa Principal

while True:
    n = input()
    if n == '-1':
        break
    print(*converte_base_3_a_10(n))


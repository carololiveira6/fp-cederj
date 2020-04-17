'''
Faça um programa que leia strings da entrada padrão até que a string vazia (“”) seja digitada. Suponha que cada string não vazia seja convertível em um número de ponto flutuante.
Escreva:
(1) A quantidade de strings não vazias lidas;
(2) Caso exista: a média dos valores, das strings numéricas lidas;
(3) Caso exista: o valor do maior número lido.
'''

# Programa Principal
qntStringNV = 0
somaValores = 0
maiorValor = 0
mediaValores = 0

string = True
while string != "":                  # String não vazia
    string = str(input())
    if string == "":                 # String vazia
        break                        # Programa para
    try:
        string = float(string)       # Converte String para Ponto
        if type(string) == float:
            somaValores += string
            qntStringNV += 1
            mediaValores = somaValores / qntStringNV
        if string > maiorValor:
            maiorValor = string
    except:
        break
print(f'Quantidade de Números: {qntStringNV}')
print(f'Média dos Números: {mediaValores}')
print(f'Maior: {maiorValor}')

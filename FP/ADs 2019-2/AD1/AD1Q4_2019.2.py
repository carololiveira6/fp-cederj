'''
A conversão de números inteiros para diferentes bases é uma operação realizada frequentemente em computação. Por exemplo, no dia a dia estamos habituados a trabalhar com números na base decimal. Entretanto, o computador opera na base binária. Enquanto, eventualmente, a inspeção visual do conteúdo da memória do computador é feita na base octal ou hexadecimal.
Faça um programa que, dados valores inteiros na binária, escreva na saída padrão cada valor convertido para as bases 3 a 10.
Seu programa deve conter um subprograma que respeite o seguinte protótipo:
def converte(numBinario, base):
...
return numConvertido
3
Entrada
A entrada é composta por várias linhas, cada uma contando um valor inteiro binário não negativo com até 8 dígitos. A última linha contém o valor -1, que não deve ser processado.
Saída
Uma linha deve ser emitida na saída padrão para cada valor dado como entrada. Essa linha deve conter as oito representações do número, uma para cada base, separados por um espaço em branco. As conversões devem ser apresentadas em ordem crescente de base.
Restrições
Não é permitido o uso de rotinas de conversão nativas do Python.
'''



def converte (numBinario):
    numConvertido = 0
    vet = list(numBinario)
    vet.reverse()
    for i in range(len(vet)):
        numConvertido = (int(vet[i]) * (2 ** i)) + numConvertido
    return numConvertido

def converteBases (m, base):
    if m == 0:
        return '0'
    numeros = []
    while m:
        m, n = divmod(m, base)
        numeros.append(str(n))
    return ''.join(reversed(numeros))


entrada = input()
if entrada != '-1':
    for i in range(3,10):
        print(converteBases(converte(entrada),i), end=' ')
    print(converte(entrada))



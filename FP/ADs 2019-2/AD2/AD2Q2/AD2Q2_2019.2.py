def numPrimo(num):
    numDivisores = 0
    i = 1
    while i <= num:
        if num % i == 0:
            numDivisores += 1
        i = i + 1
    if numDivisores == 2:
        return True
    else:
        return False


arquivoEntrada = input('Digite o nome do arquivo de entrada: ')
arquivoSaida = input('Digite o nome do arquivo de saída: ')
arqEntrada = open(arquivoEntrada, 'r', encoding='utf8')
arqSaida = open(arquivoSaida, 'w', encoding='utf8')
with arqEntrada as entrada, arqSaida as saida:
    for linhaNum in entrada:
        linhaNum = linhaNum.strip()
        numeros = linhaNum.split()
        numPrimos = []
        for i in numeros:
            if numPrimo(int(i)):
                numPrimos.append(i)
        novaLinha = ' '.join(numPrimos)
        saida.write(f'{novaLinha}\n')


def palindromo(palavra):
    if len(palavra) <= 1:
        return True
    primeiraLetra = palavra[0]
    ultimaLetra = palavra[-1]
    if primeiraLetra != ultimaLetra:
        return False
    return palindromo(palavra[1:-1])


arquivoTexto = input('Digite o nome do arquivo de entrada: ')
with open(arquivoTexto, 'r', encoding='utf8') as arquivo:
    for cadaFrase in arquivo:
        cadaFrase = cadaFrase.strip()
        cadaPalavra = cadaFrase.split()
        for palavra in cadaPalavra:
            if palindromo(palavra):
                print(palavra)
def main() -> None:
    operador = input()
    operando1 = input()
    operando2 = input()
    n_linhas = int(input())

    # entrada das linhas:
    i = 0
    linhas = []
    while i != n_linhas:
        linhas.append(str(input()))
        i += 1
    str_codificada = ''.join(linhas)

    # define o operando1:
    if operando1 == "vogal":
        posicao1 = primeira_vogal(0, str_codificada)
    elif operando1 == "consoante":
        posicao1 = primeira_consoante(0, str_codificada)
    elif operando1 == "numero":
        posicao1 = primeiro_numero(0, str_codificada)
    else:
        posicao1 = ache_o_caractere(operando1, str_codificada)

    # define o operando2:
    if operando2 == "vogal":
        posicao2 = primeira_vogal(posicao1, str_codificada)
    elif operando2 == "consoante":
        posicao2 = primeira_consoante(posicao1, str_codificada)
    elif operando2 == "numero":
        posicao2 = primeiro_numero(posicao1, str_codificada)
    else:
        posicao2 = ache_o_caractere(operando2, str_codificada[posicao1:]) + posicao1

    # define e executa a operação para obter k:
    if operador == "+":
        k = posicao1 + posicao2
    elif operador == "-":
        k = posicao1 - posicao2
    elif operador == "*":
        k = posicao1 * posicao2
    print(k)

    # decodificação:
    for linha in linhas:
        temp = []
        for j in range(len(linha)):
            asc2_codificado = ache_na_asc2(linha[j])  # numero da asc2 que veio no input(codificado)
            asc2_decodificado = asc2_codificado + k  # numero da asc2 decodificado
            caractere_decodificado = asc2_para_caractere(asc2_decodificado)  # caractere do numero decodificado
            temp.append(caractere_decodificado)
        linha = ''.join(temp)
        print(linha)


def ache_o_caractere(caractere: str, texto: str) -> int:
    '''retorna a posição da primeira aparição de um caractere em um texto'''

    return texto.find(caractere)


def primeiro_numero(referencia: int, texto: str) -> int:
    '''retorna a primeira aparição de um numero inteiro depois de uma referncia em um texto'''

    numero = '0123456789'
    texto = texto[referencia:]
    temp = [texto.find(i) for i in numero if texto.find(i) != -1]
    temp.sort()
    return (temp[0] + referencia)


def primeira_vogal(referencia: int, texto: str) -> int:
    '''retorna a primeira aparição de uma vogal depois de uma referência em um texto'''

    vogais = 'aeiouAEIOU'
    texto = texto[referencia:]
    temp = [texto.find(i) for i in vogais if texto.find(i) != -1]
    temp.sort()
    return (temp[0] + referencia)


def primeira_consoante(referencia: int, texto: str) -> int:
    '''retorna a primeira aparição de uma consoante depois de uma referncia em um texto'''

    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    texto = texto[referencia:]
    temp = [texto.find(i) for i in consoantes if texto.find(i) != -1]
    temp.sort()
    return (temp[0] + referencia)


def ache_na_asc2(caractere: str) -> int:  # até o 126 no caso
    '''retorna o numero da asc2 (do 32 até o 126) de um caractere'''

    return ord(caractere)


def asc2_para_caractere(codigo_asc2: int) -> str:
    '''retorna o caractere referente a um numero da tabela asc2 de 32 até 126'''
    
    while codigo_asc2 > 126:
        codigo_asc2 -= 95
    while codigo_asc2 < 32:
        codigo_asc2 += 95
    return chr(codigo_asc2)


if __name__ == "__main__":
    main()

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
    if len(operando1) == 1:
        posicao1 = ache_o_caractere(operando1, str_codificada)
    else:
        posicao1 = primeiro_do_tipo(0, operando1, str_codificada)

    # define o operando2:
    if len(operando2) == 1:
        posicao2 = ache_o_caractere(operando2, str_codificada[posicao1:]) + posicao1
    else:
        posicao2 = primeiro_do_tipo(posicao1, operando2, str_codificada)

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


def primeiro_do_tipo(referencia: int, tipo: str, texto: str) -> int:
    '''retorna a primeira aparição de um tipo (numero, vogal ou consoante) depois de uma referncia em um texto'''

    if tipo == 'numero':
        comparacao = '0123456789'
    elif tipo == 'vogal':
        comparacao = 'aeiouAEIOU'
    elif tipo == 'consoante':
        comparacao = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    texto = texto[referencia:]
    temp = [texto.find(i) for i in comparacao if texto.find(i) != -1]
    temp.sort()
    return (temp[0] + referencia)



def ache_na_asc2(caractere: str) -> int:  # até o 126 no caso
    '''retorna o numero da asc2 (do 32 até o 126) de um caractere'''

    asc2 = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
    return (asc2.find(caractere) + 32)


def asc2_para_caractere(codigo_asc2: int) -> str:
    '''retorna o caractere referente a um numero da tabela asc2 de 32 até 126'''
    
    asc2 = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
    while codigo_asc2 > 126:
        codigo_asc2 -= 95
    while codigo_asc2 < 32:
        codigo_asc2 += 95
    return asc2[codigo_asc2 - 32]


if __name__ == "__main__":
    main()

def main():
    sala = []
    for i in range(int(input())):
        sala.append(input().split())
    printa_sala(sala)
    escaneia_sala(sala)


def escaneia_sala(sala: list):
    '''compara o "r" com o que está na frente (ou abaixo), se limpo, 
    troca de lugar o r e imprime a nova sala, se tetiver sujeira chama
    o modo de limpeza'''
    linhas = len(sala)
    colunas = len(sala[0])
    if sala[-1][-1] == 0:
        return None

    for linha in range(linhas):
        # para linhas pares:
        if linha % 2 == 0:
            for coluna in range(colunas):
                if sala[linha][coluna] == 'r' and coluna < colunas - 1 and linha != linhas -1:
                    if sala[linha][coluna + 1] == '.' and sala[linha + 1][coluna] == '.':
                        sala[linha][coluna] = '.'
                        sala[linha][coluna + 1] = 'r'
                        printa_sala(sala)
                    elif sala[linha][coluna + 1] == 'o':  # se tiver na direita
                        limpa_sala(sala, linha, coluna + 1, linha, coluna)
                        return None
                    elif sala[linha + 1][coluna] == 'o':  # se tiver em baixo
                        limpa_sala(sala, linha, coluna, linha, coluna)
                        return None
                elif coluna == colunas - 1 and linha != linhas - 1 and sala[-1][-1] != 'r':  # qnd chegar no último
                        if sala[linha + 1][coluna] == '.': # se em baixo estiver limpo
                            sala[linha + 1][coluna] = 'r'
                            sala[linha][coluna] = '.'
                            printa_sala(sala)
                        elif sala[linha + 1][coluna] == 'o': # se em baixo estiver sujo
                            limpa_sala(sala, linha, coluna, linha, coluna)
                            return None
                elif linha == linhas - 1 and coluna == 0:
                    finaliza(sala)
        # para linhas ímpares:
        else:
            for coluna in range(colunas - 1, -1, -1):
                if sala[linha][coluna] == 'r':
                    if sala[linha][coluna - 1] == '.' and sala[linha + 1][coluna] == '.' and coluna != 0:
                        sala[linha][coluna - 1] = 'r'
                        sala[linha][coluna] = '.'
                        printa_sala(sala)
                    elif sala[linha][coluna - 1] == 'o' and coluna != 0: # se tiver na esquerda
                        limpa_sala(sala, linha - 1, coluna, linha, coluna)
                        return None
                    elif linha != len(sala) - 1 and sala[linha + 1][coluna] == 'o':  # se tiver em baixo
                        limpa_sala(sala, linha + 1, coluna, linha, coluna)
                        return None
                    elif coluna == 0 and linha != linhas - 1:  # qnd chegar no primeiro
                        if sala[linha + 1][coluna] == '.': # se em baixo estiver limpo
                            sala[linha + 1][coluna] = 'r'
                            sala[linha][coluna] = '.'
                            printa_sala(sala)
                        elif sala[linha + 1][coluna] == 'o': # se em baixo estiver sujo
                            limpa_sala(sala, linha + 1, coluna, linha, coluna)
                            return None
                    elif coluna == 0 and linha == linhas - 1:
                        finaliza(sala)


def limpa_sala(sala: list, linha_r: int, coluna_r: int) -> list:

    i = 0
    while i == 0:
        if coluna_r != 0 and sala[linha_r][coluna_r - 1] == 'o':  # esquerda
            sala[linha_r][coluna_r - 1] = 'r'
            sala[linha_r][coluna_r] = '.'
            printa_sala(sala)

        elif linha_r != 0 and sala[linha_r - 1][coluna_r] == 'o':  # cima
            sala[linha_r - 1][coluna_r] = 'r'
            sala[linha_r][coluna_r] = '.'
            printa_sala(sala)

        elif coluna_r != len(sala[linha_r]) - 1 and sala[linha_r][coluna_r + 1] == 'o':  # direita
            sala[linha_r][coluna_r + 1] = 'r'
            sala[linha_r][coluna_r] = '.'
            printa_sala(sala)

        elif linha_r != len(sala) - 1 and sala[linha_r + 1][coluna_r] == 'o':  # baixo
            sala[linha_r + 1][coluna_r] = 'r'
            sala[linha_r][coluna_r] = '.'
            printa_sala(sala)
        
        else:
            i, j = acha_robo(sala)
            if i == linha_r and j == coluna_r:
                escaneia_sala(sala)
                i = 1
            else:
                retorna_inicial(sala, i, j, linha_r, coluna_r)
                i = 1
    return None


def acha_robo(sala: list) -> tuple:
    linhas = len(sala)
    colunas = len(sala[0])
    for i in range(linhas):
        for j in range(colunas):
            if sala[i][j] == 'r':
                return i, j
            

def retorna_inicial(sala, l_atual, c_atual, l_destino, c_destino):
    i = 0
    while i == 0:
        if c_atual < c_destino:  # vai pra direita
            sala[l_atual][c_atual] = '.'
            sala[l_atual][c_atual + 1] = 'r'
            printa_sala(sala)
            c_atual += 1
        elif c_atual > c_destino:  # vei pra esquerda
            sala[l_atual][c_atual] = '.'
            sala[l_atual][c_atual - 1] = 'r'
            printa_sala(sala)
            c_atual -= 1
        else:
            if l_atual < l_destino:  # vai pra baixo
                sala[l_atual][c_atual] = '.'
                sala[l_atual + 1][c_atual] = 'r'
                printa_sala(sala)
                l_atual += 1
            elif l_atual > l_destino:  # vai pra cima
                sala[l_atual][c_atual] = '.'
                sala[l_atual - 1][c_atual] = 'r'
                printa_sala(sala)
                l_atual -= 1
            else:
                i = 1
    escaneia_sala(sala)
    return None


def finaliza(sala: list):
    if sala[-1][-1] == 'r':
        return None
    else:
        for spot in range(len(sala[-1]) - 1):
            sala[-1][spot] = '.'
            sala[-1][spot + 1] = 'r'
            printa_sala(sala)
        return None


def printa_sala(sala: list) -> str:
    '''printa de maneira bonitinha a sala'''
    for corredor in sala:
        for spot in range(len(corredor)):
            if spot != len(corredor) - 1:
                print(corredor[spot], '', end='')
            else:
                print(corredor[spot], end='')
        print()
    if sala[-1][-1] != 'r':
        print()
    

if __name__ == "__main__":
    main()
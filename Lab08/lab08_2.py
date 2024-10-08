def main():
    numero_de_filmes = int(input())
    i = 0
    filmes = []
    while i != numero_de_filmes:
        filme = str(input())
        filmes.append(filme)
        i += 1
    numero_de_avaliacoes = int(input())
    i = 0
    avaliacoes = []
    while i != numero_de_avaliacoes:
        avaliacoes.append(str(input()).split(', '))
        i += 1
    #print(filmes)
    #print(avaliacoes)
    for avaliacao in avaliacoes:
        if avaliacao[1] == 'filme que causou mais bocejos':
            for filme in  filmes:
                
        elif avaliacao[1] == 'filme que foi mais pausado':
            print()
        elif avaliacao[1] == 'filme que mais revirou olhos':
            print()
        elif avaliacao[1] == 'filme que não gerou discussão na redes sociais':
            print()
        elif avaliacao[1] == 'enredo mais sem noção':
            print()

def cria_dicionario(dicionario: dict, chaves: list, valores: list):
    dicionario = dict(zip(chaves, valores))
    return dicionario


if __name__ == '__main__':
    main()
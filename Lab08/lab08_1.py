def main():
    categorias = {'filme que causou mais bocejos' : dict(),
                  'filme que foi mais pausado' : dict(),
                  'filme que mais revirou olhos' : dict(),
                  'filme que não gerou discussão nas redes sociais': {},
                  'enredo mais sem noção': {}}

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
'''
    for filme in filmes:
        for categoria in categorias:
            categorias[categoria[filme]] = filme
    print(categorias)

    for avaliacao in avaliacoes:
        categorias[avaliacao[1]][]
'''

    for categoria in  categorias:
        cria_chaves(categoria, filmes, )

def cria_chaves(dicionario: dict, chaves: list[str], valores: list[str]):
    dicionario = dict(zip(chaves, valores))
    return



if __name__ == '__main__':
    main()
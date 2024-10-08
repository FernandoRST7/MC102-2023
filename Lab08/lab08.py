# Labs\Lab08\lab08.py

def main():
    #dicionario com categorias e suas respectivas notas(futuras)
    categorias = {'filme que causou mais bocejos': [],
                  'filme que foi mais pausado': [],
                  'filme que mais revirou olhos': [],
                  'filme que não gerou discussão nas redes sociais': [],
                  'enredo mais sem noção': []}
    
    # cria dicionario de filmese e atribui a eles as categporias e suas notas(futuras)
    numero_de_filmes = int(input())
    filmes: dict[str, dict[str, list[int]]] = {}
    for _ in range(numero_de_filmes):
        filme = input()
        filmes[filme] = copia(categorias)

    # adiciona as notas às listas de notas(não mais futuras)
    numero_de_avaliacoes = int(input())
    entradas = []
    for _ in range(numero_de_avaliacoes):
        avaliacao = list(str(input()).split(', '))
        filmes[avaliacao[2]][avaliacao[1]].append(int(avaliacao[3]))
        entradas.append(avaliacao)
    
    # troca listas de notas por media em outro dicionario
    medias_filmes = copia(filmes)
    #for entrada in entradas:
    #    medias_filmes[entrada[2]][entrada[1]] = media(filmes[entrada[2]][entrada[1]])
    for f in filmes:
        for c in categorias:
            medias_filmes[f][c] = media(medias_filmes[f][c])

    # categorias simples
    vencedor_categorias = copia(categorias)
    for catg in categorias:
        # encontra qual a maior média para categoria em analise
        media_maior = 0.0
        for film in medias_filmes:
            if medias_filmes[film][catg] >= media_maior:
                media_maior = medias_filmes[film][catg]
        
        # define como vencedor(es) da categoria por maior média
        for film in medias_filmes:
            if medias_filmes[film][catg] == media_maior:
                vencedor_categorias[catg].append(film)
    
    # define vencedor diferenciando para: único; mais de um; nenhum
    # vencedor_categorias[categoria] é uma chave que leva a uma lista de filmes (list[str])
    # essa chave passará a entregar o nome do filme vencedor (que é uma str)
    for categoria in vencedor_categorias:
        if len(vencedor_categorias[categoria]) == 1:  # único vencedor
            vencedor_categorias[categoria] = vencedor_categorias[categoria][0]

        elif len(vencedor_categorias[categoria]) > 1:  # empatado
            avaliacoes = []
            for vencedor in vencedor_categorias[categoria]:
                avaliacoes.append(len(filmes[vencedor][categoria]))  # adiciona em ordem o numero de avaliações dos filmes empatados
            mais_avaliado = max(avaliacoes)
            posicao_mais_avaliado = avaliacoes.index(mais_avaliado)  # da a posição do mais avaliado
            vencedor_categorias[categoria] = vencedor_categorias[categoria][posicao_mais_avaliado]

        elif len(vencedor_categorias[categoria]) == 0:  # sem vencedores
            vencedor_categorias[categoria] = 'sem vencedores'
    
    # categoria especial:
    vencedores_simples = list(vencedor_categorias.values())  # lista com os filmes vencedores
    vitorias = []
    for vencedo in vencedores_simples:
        vitorias.append(vencedores_simples.count(vencedo))

    if vitorias.count(max(vitorias)) >= 2:  # empate
        empatados = []
        maximo = max(vitorias)
        for _ in range(vitorias.count(maximo)):
            empatados.append(vencedores_simples[vitorias.index(maximo)])
            del  vencedores_simples[vitorias.index(maximo)], vitorias[vitorias.index(maximo)]
        pontuacao = []
        for empatado in empatados:
            pontuacao.append(sum(list(medias_filmes[empatado].values())))
        vencedor_especial = empatados[pontuacao.index(max(pontuacao))]
    
    elif vitorias.count(max(vitorias)) == 1:
        vencedor_especial = vencedores_simples[vitorias.index(max(vitorias))]

    # não merecia estar aqui:
    nao_merecia = []
    for movie in medias_filmes:
        if sum(medias_filmes[movie].values()) == 0:
            nao_merecia.append(movie)

    # printando:
    print('#### abacaxi de ouro ####')
    print()
    print('categorias simples')
    
    print('categoria: filme que causou mais bocejos')
    print('-', vencedor_categorias['filme que causou mais bocejos'])
    
    print('categoria: filme que foi mais pausado')
    print('-', vencedor_categorias['filme que foi mais pausado'])
    
    print('categoria: filme que mais revirou olhos')
    print('-', vencedor_categorias['filme que mais revirou olhos'])
    
    print('categoria: filme que não gerou discussão nas redes sociais')
    print('-', vencedor_categorias['filme que não gerou discussão nas redes sociais'])
    
    print('categoria: enredo mais sem noção')
    print('-', vencedor_categorias['enredo mais sem noção'])
    
    print()
    print('categorias especiais')
    print('prêmio pior filme do ano')
    print('-', vencedor_especial)
    print('prêmio não merecia estar aqui')
    
    if len(nao_merecia) == 0:
        print('- sem ganhadores')
    elif len(nao_merecia) == 1:
        print('-', nao_merecia[0])
    else:
        print('- ', end="")
        if len(nao_merecia) > 1:
            for nao_merecedor in nao_merecia:
                print(nao_merecedor, end='')
                if nao_merecia.index(nao_merecedor) != len(nao_merecia)-1:
                    print(', ', end='')


def media(lista: list[int]) -> float:
    '''pega os números de uma lista de números e retorna uma média aritimética dos mesmos.'''
    if len(lista) == 0:
        return 0.0
    else:
        return sum(lista)/len(lista)

def copia(dicionario: dict) -> dict:
    '''cria uma copia para não mudar o original'''
    novo_dicionario = {}
    for chave, valor in dicionario.items():
        if isinstance(valor, dict):
            novo_dicionario[chave] = copia(valor)
        elif isinstance(valor, list):
            novo_dicionario[chave] = valor.copy()
        else:
            novo_dicionario[chave] = valor
    return novo_dicionario


if __name__ == "__main__":
    main()
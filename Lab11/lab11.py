'''tudo q ta com tuple vc vai ter q consertar'''
class personagem:
    '''classe para aquele que movimentara em zigue zage, no caso só o zelda xDDD'''
    def __init__(self, vida: int, dano: int, posicao: list[int]):
        self.vida = vida
        self.dano = dano
        self.posicao = posicao
    
    def desce(self):
        self.posicao[0] += 1
        return self.posicao
    
    def direita(self):
        self.posicao[1] += 1
        return self.posicao
    
    def esquerda(self):
        self.posicao[1] -= 1
        return self.posicao
    
    def sobe(self):
        self.posicao[0] -= 1
        return self.posicao
                

class monstro:
    '''classe para os monstros'''
    def __init__(self, vida: int, ataque: int, tipo: str, posicao: list[int]):
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.posicao = posicao
    
    def movimenta(self, dungeon: list[list]):
        '''vai dae out of range, conserta'''
        if self.tipo == "U":
            self.posicao[0] -= 1
        elif self.tipo == "R":
            self.posicao[1] += 1
        elif self.tipo == "D":
            self.posicao[0] += 1
        elif self.tipo == "L":
            self.posicao[1] -= 1
        return self.posicao


class objeto:
    '''classe par os objetos, como artefatos de vida ou de dano'''
    def __init__(self, nome: str, tipo: str, posicao: list[int], status: int):
        self.nome = nome
        self.tipo = tipo
        self.posicao = posicao
        self.status = status


def main():
    # inputs + desenho do mapa inicial:
    vida_dano = list(map(int, list(input().split())))
    dados_matriz = list(map(int, list(input().split())))
    dungeon = cria_dungeon(dados_matriz[0], dados_matriz[1])
    posicao_inicial_link = list(map(int, list(input().split(','))))
    
    posicao_saida = list(map(int, list(input().split(','))))
    dungeon[posicao_saida[0]][posicao_saida[1]] = '*'

    link = personagem(vida_dano[0], vida_dano[1], posicao_inicial_link)
    dungeon[link.posicao[0]][link.posicao[1]] = 'P'

    # cria e armazena os montros em um dicionario
    monstros = {}
    numero_monstros = int(input())
    for i in range(numero_monstros):
        dados = list(input().split())
        monstros[i] = monstro(dados[0], dados[1], dados[2], list(map(int, list(dados[3].split(',')))))
        im,jm = monstros[i].posicao
        dungeon[im][jm] = monstros[i].tipo
    
    # cria e armazena os objetos em um dicionario
    objetos = {}
    numero_objetos = int(input())
    for i in range(numero_objetos):
        dados = list(input().split())
        objetos[i] = objeto(dados[0], dados[1], list(map(int, list(dados[2].split(',')))), int(dados[3]))
        io, jo = objetos[i].posicao
        dungeon[io][jo] = objetos[i].tipo
    printa_matriz(dungeon)

    # começa o ciclo:
    descendo = True
    while link.vida > 0 and link.posicao != posicao_saida:
        # movimentação do link (só é pra fazer um movimento):
        # se não estiver na última linha desce
        if link.posicao == posicao_inicial_link and descendo:
            if link.posicao[0] < (len(dungeon) - 1):
                i0, j0 = link.posicao
                dungeon[i0][j0] = '.'
                i1, j1 = link.desce()
                dungeon[i1][j1] = 'P'
            else:
                descendo = False
        
        # teoricamente esta na ultima linha
        if not descendo:
            # se estiver em ímpar par vai pra direita
            if link.posicao[1]%2 != 0:
                # mas só se não for o limite
                if link.posicao[1] < len(dungeon[0]) - 1:
                    i0, j0 = link.posicao
                    dungeon[i0][j0] = '.'
                    i1, j1 = link.direita()
                    dungeon[i1][j1] = 'P'
            # se estiver em par par vai pra esquerda
            elif link.posicao[1]%2 == 0:
                # mas só se não for o limite
                if link.posicao[1] > 0:
                    i0, j0 = link.posicao
                    dungeon[i0][j0] = '.'
                    i1, j1 = link.esquerda()
                    dungeon[i1][j1] = 'P'
            # se atingir um limite sobe
            elif link.posicao[1] < len(dungeon[0]) - 1 or link.posicao[1]%2 == 0:
                # mas só se n for o limite
                if link.posicao[0] > 0:
                    i0, j0 = link.posicao
                    dungeon[i0][j0] = '.'
                    i1, j1 = link.sobe()
                    dungeon[i1][j1] = 'P'

        # movimentação dos monstros (cada um deve fazer um movimento):
        for i in monstros:
            monstros[i].movimenta(dungeon)
        
        # movimentação concluída
        atualiza(dungeon, monstros, objetos, link, posicao_saida)

        # começam as interações:
        for i in objetos:
            # se encontrar algum artefato
            if link.posicao == objetos[i].posicao:
                # se for um objeto de vida
                if objetos[i].tipo == 'v':
                    link.vida += objetos[i].status
                    if link.vida <= 0:
                        dungeon[link.posicao[0]][link.posicao[1]] = 'X'
                        atualiza(dungeon, monstros, objetos, link, posicao_saida)
                        printa_matriz(dungeon)
                        break
                # se for um objeto de dano
                elif objetos[i].tipo == 'd':
                    link.dano += objetos[i].status
                    if link.dano < 1:
                        link.dano = 1
        
        for i in monstros:
            # se trombar em algum monstro
            if link.posicao == monstros[i].posicao:
                # combate
                monstros[i].vida -= link.dano
                if monstros[i].vida > 0:
                    link.vida -= monstros[i].dano
                    if link.vida <= 0:
                        dungeon[link.posicao[0]][link.posicao[1]] = 'X'
                        atualiza(dungeon, monstros, objetos, link, posicao_saida)
                        printa_matriz(dungeon)
                        break
        
        atualiza(dungeon, monstros, objetos, link, posicao_saida)
        printa_matriz(dungeon)

        if link.posicao == posicao_saida and link.vida > 0:
            print('Chegou ao fim!')

def cria_dungeon(linhas, colunas):
    corredores = []
    dungeon = []
    for _ in range(colunas):
        corredores.append('.')
    for _ in range(linhas):
        dungeon.append(corredores.copy())
    return dungeon


def printa_matriz(matriz: list) -> str:
    '''printa de maneira bonitinha a sala'''
    for linha in matriz:
        for coluna in range(len(linha)):
            if coluna != len(linha) - 1:
                print(linha[coluna], '', end='')
            else:
                print(linha[coluna], end='')
        print()


def atualiza(dungeon: list[list], monstros: dict[int: monstro], 
             objetos: dict[int: objeto], hero: personagem, saida: tuple) -> list[list]:
    '''realoca os monstros, itens e o link conforme as informações fornecidas'''
    # mostra com menor prioridade os objetos
    for i in objetos:
        io, jo = objetos[i].posicao
        dungeon[io][jo] = objetos[i].tipo
    # depois os monstros
    for i in monstros:
        im,jm = monstros[i].posicao
        dungeon[im][jm] = monstros[i].tipo
    # a saída é a segunda coisa mais importante
    dungeon[saida[0]][saida[1]] = '*'
    # exceto pelo zelda
    il, jl = hero.posicao
    dungeon[il][jl] = 'P'
    return dungeon


if __name__ == "__main__":
    main()
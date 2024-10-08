genoma_atual = list(str(input()))
novo_genoma = []
matches = 0

#funções:
def reverter(i, j):
    if j >= len(genoma_atual):
        j = (len(genoma_atual)-1)
    if i == 0 and j == (len(genoma_atual)-1):
        genoma_atual.reverse()
        return genoma_atual
    else:
        for l in range(0, i):
            novo_genoma.append(genoma_atual[l])
        for l in reversed(range(i, j+1)):
            novo_genoma.append(genoma_atual[l])
        for l in range(j+1, len(genoma_atual)):
            novo_genoma.append(genoma_atual[l])
        genoma_atual.clear()
        for l in range(len(novo_genoma)):
            genoma_atual.append(novo_genoma[l])
        novo_genoma.clear()
        return genoma_atual

def transpor(i, j, k):
    for l in range(0, i):
        novo_genoma.append(genoma_atual[l])
    for l in range(j+1, k+1): #segunda porção
        novo_genoma.append(genoma_atual[l])
    for l in range(i, j+1): #primeira porção
        novo_genoma.append(genoma_atual[l])
    for l in range(k+1, len(genoma_atual)):
        novo_genoma.append(genoma_atual[l])
    genoma_atual.clear()
    for l in range(len(novo_genoma)):
        genoma_atual.append(novo_genoma[l])
    novo_genoma.clear()
    return genoma_atual

def combinar(combinando, i):
    adiciona = list(combinando)
    for l in range(0, i):   #começo n mudado
        novo_genoma.append(genoma_atual[l]) 
    for l in range(0, len(adiciona)): #poe oq mandou
        novo_genoma.append(adiciona[l])
    for l in range(i, len(genoma_atual)): 
        novo_genoma.append(genoma_atual[l])
    genoma_atual.clear()
    for l in range(len(novo_genoma)):
        genoma_atual.append(novo_genoma[l])
    novo_genoma.clear()
    return genoma_atual

def concatenar(concatenando):
    adiciona = list(concatenando)
    for l in range(0, len(genoma_atual)):
        novo_genoma.append(genoma_atual[l])
    for l in range(0, len(adiciona)): 
        novo_genoma.append(adiciona[l])
    genoma_atual.clear()
    for l in range(len(novo_genoma)):
        genoma_atual.append(novo_genoma[l])
    novo_genoma.clear()
    return genoma_atual

def remover(i, j):
    for l in range(0, i):
        novo_genoma.append(genoma_atual[l])
    for l in range(j+1, len(genoma_atual)):
        novo_genoma.append(genoma_atual[l])
    genoma_atual.clear()
    for l in range(len(novo_genoma)):
        genoma_atual.append(novo_genoma[l])
    novo_genoma.clear()
    return genoma_atual

def transpor_e_reverter(i, j, k):
    temporaria = []
    #transpoe
    transpor(i, j, k)
    #inverte
    reverter(i, k)

def buscar(buscando):
    busca = list(buscando)
    genoma_str = ''.join(genoma_atual)
    temp = []
    for l in range(len(genoma_atual)):
        temp.append(genoma_atual[l])
    contador = 0
    bateu = 0
    memoria = 0
    global matches
    i = 0
    while i < len(genoma_atual):
        if buscando == genoma_str[i:i + len(busca)]:
            bateu += 1
            i += len(busca)
        else:
            i += 1
    matches = matches + bateu
    return matches

def buscar_bidirecional(buscando):
    buscar(buscando)
    reverter(0, len(genoma_atual))
    buscar(buscando)
#            if m%len(busca) == 0:
#                contador = memoria + len(busca)
#                memoria = contador
    
    reverter(0, len(genoma_atual))

#le os comandos para executar as funções:
while True:
    comando = input().split()
    if comando[0] == "reverter":
        reverter(int(comando[1]), int(comando[2]))
    elif comando[0] == "transpor":
        transpor(int(comando[1]), int(comando[2]), int(comando[3]))
    elif comando[0] == "combinar":
        combinar(comando[1], int(comando[2]))
    elif comando[0] == "concatenar":
        concatenar(comando[1])
    elif comando[0] == "remover":
        remover(int(comando[1]), int(comando[2]))
    elif comando[0] == "transpor_e_reverter":
        transpor_e_reverter(int(comando[1]), int(comando[2]), int(comando[3]))
    elif comando[0] == "buscar":
        buscar(comando[1])
        print(matches)
        matches = 0
    elif comando[0] == "buscar_bidirecional":
        buscar_bidirecional(comando[1])
        print(matches)
        matches = 0
    elif comando[0] == "mostrar":
        if len(novo_genoma) == 0:
            for l in range(len(genoma_atual)):
                print(genoma_atual[l], end='')
            print()
        else:
            for l in range(len(novo_genoma)):
                print(novo_genoma[l], end='')
            print()
    elif comando[0] == "sair":
        break

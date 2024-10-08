n_jogadores = int(input()) #numero de jogadores
n_sortidos = str(input()) #numero de cada jogador
Ln_sortidos = n_sortidos.split() #lista com os numeros dos jogadores 
Ln_sortidos_int = [] #lista com os numeros dos jogadores em int
n_limites = str(input()) #numero dos limites
Ln_limites = n_limites.split() #lista com os limites dos jogadores 
Ln_limites_int = [] #lista com os limites dos jogadores em int

#transformando str pra int:
for i in range(len(Ln_sortidos)):
    Ln_sortidos_int.append( int(Ln_sortidos[i]))

for i in range(len(Ln_limites)):
    Ln_limites_int.append( int(Ln_limites[i]))

#cálculo dos pontos:
Lpontos = []
for i in range((n_jogadores+1)//2): #para a primeira metade
    pontos = (Ln_limites_int[i*2+1] - Ln_limites_int[i*2])*Ln_sortidos_int[i]
    Lpontos.append(pontos)
for i in range((n_jogadores+1)//2, n_jogadores): #para a segunda metade
    pontos = (Ln_limites_int[i*2+1] - Ln_limites_int[i*2])+Ln_sortidos_int[i]
    Lpontos.append(pontos)

#definição do vencedor/empate:
máximo = 0
i = 0
empate = False
while i < len(Lpontos):
    if Lpontos[i]>máximo: #se o item da posição i > q o máximo anterior
        máximo = Lpontos[i] #estabelece um novo máximo
    elif Lpontos[i]==máximo:
        empate = True
        print("Rodada de cerveja para todos os jogadores!")
    i += 1
if empate == False:
    for i in range(len(Lpontos)):
        if máximo == Lpontos[i]:
            vencedor = máximo #vencedor na real é os pontos do vencedor
            print("O jogador número", i+1, "vai receber o melhor bolo da cidade pois venceu com", vencedor, "ponto(s)!") #a posição do jogador vencedor
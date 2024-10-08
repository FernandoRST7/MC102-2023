import math
def main():
    vida_max_aloy = int(input())
    vida_aloy = vida_max_aloy
    final = 'prefiro souls like, mas esse é legal tbm'
    flechas = {}
    flechas_usadas = {}
    lista_flechas = list(input().split())
    for i in range(0, len(lista_flechas), 2):
        flechas[lista_flechas[i]] = int(lista_flechas[i + 1])
        flechas_usadas[lista_flechas[i]] = 0
    flechas_data = copia(flechas)
    flechas_nao_usadas = copia(flechas_usadas)
    
    numero_maquinas = int(input())
    maquinas = {}
    
    combate_atual = 0
    # loop de combate
    # deverá qubrar se: maq derrotadas ou aloy derrotada ou 0 flechas
    while numero_maquinas != 0:
        combates = int(input())
        combateu = combates
        
        # cura
        cura = math.floor(0.5*vida_max_aloy)
        vida_aloy = vida_aloy + cura
        if vida_aloy > vida_max_aloy:
            vida_aloy = vida_max_aloy
        
        #flechas recolhidas
        flechas = copia(flechas_data)
        flechas_usadas = copia(flechas_nao_usadas)

        # entra os status da(s) maquina(s) que entrarão em combate
        for i in range(combates):
            maquinas[i] = {}
            status_maq = list(input().split())
            maquinas[i]['vida'] = int(status_maq[0])
            maquinas[i]['ATK'] = int(status_maq[1])
            numero_partes = int(status_maq[2])
            for __ in range(numero_partes):
                partes_maq = list(input().split(', '))
                maquinas[i][partes_maq[0]] = {}
                maquinas[i][partes_maq[0]]['fraqueza'] = partes_maq[1]
                maquinas[i][partes_maq[0]]['dano max'] = int(partes_maq[2])
                maquinas[i][partes_maq[0]]['coordenadas'] = (int(partes_maq[3]), int(partes_maq[4]))

        # combate comça
        criticos = {}
        numero_criticos = 0
        vida_pre_combate = vida_aloy
        combatendo = True
        maquinas_combatidas = []

        while sum(list(flechas.values())) >= 0 and vida_aloy > 0 and combatendo == True:
            # aloy atira 3 flechas
            for atk in range(3):
                if combateu <= 0:
                    break
                ataque = list(input().split(', '))
                if maquinas[int(ataque[0])]['vida'] > 0:
                    critico = False
                    if maquinas[int(ataque[0])][ataque[1]]['fraqueza'] == ataque[2] or maquinas[int(ataque[0])][ataque[1]]['fraqueza'] == 'todas':
                        critico = True
                    if (int(ataque[3]), int(ataque[4])) == maquinas[int(ataque[0])][ataque[1]]['coordenadas']:  # "critico verdadeiro"
                        criticos[numero_criticos] = (int(ataque[3]), int(ataque[4]))
                        numero_criticos += 1
                    maquinas[int(ataque[0])]['vida'] = maquinas[int(ataque[0])]['vida'] - dano(critico,
                                                                                    maquinas[int(ataque[0])][ataque[1]]['dano max'],
                                                                                    maquinas[int(ataque[0])][ataque[1]]['coordenadas'],
                                                                                    (int(ataque[3]), int(ataque[4])))
                    flechas[ataque[2]] -= 1
                    flechas_usadas[ataque[2]] += 1
                    if maquinas[int(ataque[0])]['vida'] <= 0:
                        numero_maquinas -= 1
                        combateu -= 1
                        maquinas_combatidas.append(int(ataque[0]))
                    if sum(list(flechas.values())) <= 0:
                        final = "Aloy ficou sem flechas e recomeçará sua missão mais preparada."
                        combateu = 0
                
            # turno de atk das maquinas
            for i in range(combates):
                if maquinas[i]['vida'] > 0:
                    vida_aloy -= maquinas[i]['ATK']
            if vida_aloy <= 0:
                final = "Aloy foi derrotada em combate e não retornará a tribo."
                vida_aloy = 0
            if combateu == 0 or sum(list(flechas.values())) <= 0 or vida_aloy <= 0:  # final do combate
                combatendo = False
            # fim do combate
            vida_pos_combate = vida_aloy
            
        # resultado do combate
        print("Combate ", combate_atual, ', vida = ', vida_pre_combate, sep='')
        if combateu < combates:
            for combatida in maquinas_combatidas:
                print("Máquina ", combatida, " derrotada", sep='')
        print("Vida após o combate = ", vida_pos_combate, sep='')
        
        if vida_aloy > 0 and final != "Aloy ficou sem flechas e recomeçará sua missão mais preparada.":
            print("Flechas utilizadas:", sep='')
            for flecha in flechas_usadas:
                if flechas_usadas[flecha] != 0:
                    print("- ", flecha, ": ", flechas_usadas[flecha], '/', flechas_data[flecha], sep='')
            # críticos
            if numero_criticos > 0:
                print("Críticos acertados:", sep='')
                print("Máquina ", combateu, ":", sep='')
                spots = []
                spots_conjunto = set()
                for ponto in list(criticos.values()):
                    spots.append(list(criticos.values()).count(ponto))
                    spots_conjunto.add(ponto)
                spots2 = list(spots_conjunto)
                for crit in range(len(spots_conjunto)):
                    print('- ', spots2[crit], ': ', spots[crit], 'x', sep='')
        elif vida_aloy <= 0:
            print("Aloy foi derrotada em combate e não retornará a tribo.")
            break
        elif final == "Aloy ficou sem flechas e recomeçará sua missão mais preparada.":
            print(final)
            break
        combate_atual += 1

    if numero_maquinas <= 0 and vida_max_aloy > 0:
        final = "Aloy provou seu valor e voltou para sua tribo."
        print(final)
    numero_maquinas = 0


def dano(critico, dano_max: int,
          xy_critico: tuple, xy_atingido: tuple)-> int:
    '''calcula o dano'''
    xc, yc = xy_critico
    xa, ya = xy_atingido
    dano = round(abs(dano_max - (abs(xc - xa) + abs(yc - ya))))
    if critico:
        return int(dano)
    else:
        return int(dano//2)


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
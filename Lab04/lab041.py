def lista_multiplas_entradas(nome_lista, entradas): 
    for j in range(entradas):
        nome_entrada = str(input()).split() #lista com um grupo
        for i in range(len(nome_entrada)):
            nome_lista.append(nome_entrada[i]) #junta todos os grupos
    return nome_lista

def str_int(lista_strs, lista_final):
    for i in range(len(lista_strs)//2):
        lista_final.append(lista_strs[i*2]) #primeiro mantem str
        lista_final.append(int(lista_strs[i*2+1])) #o depois dele muda pra int
    return lista_final

#entradas:
D = int(input()) #númerod e dias analisados

#execução:
for g in range(D):
    M = int(input()) #quantidade de pares de animais que brigam
    Lista_briguentos = [] #lista com todos os pares
    Lista_briguentos = lista_multiplas_entradas(Lista_briguentos, M)
    proc_quant = (input()).split() #entra com P e Q
    proc_quant_n_int = []
    str_int(proc_quant, proc_quant_n_int)
    Z = int(input()) #quantos animais compareceram
    Lista_animais_proc = []
    lista_multiplas_entradas(Lista_animais_proc,Z) #lista com os animais e solicitações
    Lista_animais_presentes = []
    for i in range(len(Lista_animais_proc)//2):
        Lista_animais_presentes.append(Lista_animais_proc[i*2]) #separa os animais das solicitações

    print('Dia:', g+1)
    #contagem das brigas:
    quantas_brigas = 0
    for i in range(len(Lista_animais_proc)//2):
       for j in range(len(Lista_briguentos)//2):
            if Lista_animais_proc[i*2] == Lista_briguentos[j*2]:
                for k in range(len(Lista_briguentos)):
                    if Lista_animais_proc[k*2] == Lista_briguentos[j*2+1]:
                        quantas_brigas += 1
    print('Brigas:', quantas_brigas)

    #atendido ou não:
    Lista_atendidos = []
    Lista_nao_atendidos = []
    Lista_nao_fornecidos = []
    
    for i in range(len(Lista_animais_proc)//2):
        contador = 0
        for j in range(len(proc_quant_n_int)//2):
            if Lista_animais_proc[i*2+1] == proc_quant_n_int[j*2]: #acha o procedimento
                if proc_quant_n_int[j*2+1] > 0: #se ele estiver disponível
                    proc_quant_n_int[j*2+1] -= 1
                    Lista_atendidos.append(Lista_animais_proc[i*2])
                else:
                    Lista_nao_atendidos.append(Lista_animais_proc[i*2])
            else:
                contador += 1 #conta quantos diferentes foram
        if contador == len(proc_quant_n_int)//2: #se o requisitado for diferente de todos os disponíveis
            Lista_nao_fornecidos.append(Lista_animais_proc[i*2])

    print('Animais atendidos: ', end='')
    for i in range(len(Lista_atendidos)):
        print(Lista_atendidos[i],  end='')
        if i == len(Lista_atendidos)-1:
            print(end='')
            print()
        else:
            print(', ', end='')
    if len(Lista_nao_atendidos) != 0:
        print('Animais não atendidos: ', end='')
        for i in range(len(Lista_nao_atendidos)):
            print(Lista_nao_atendidos[i], end='')
            if i == len(Lista_nao_atendidos)-1:
                print(end='')
                print()
            else:
                print(', ', end='')
    if len(Lista_nao_fornecidos) != 0:
        for i in range(len(Lista_nao_fornecidos)):
            print('Animal', Lista_nao_fornecidos[i], 'solicitou procedimento não disponível.')
    print()
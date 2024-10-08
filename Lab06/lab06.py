# flake8: python -m flake8 Labs\Lab06\lab06.py
# Mypy: python -m mypy --strict Labs\Lab06\lab06.py
# vetor -> vet; lista -> L; vetor_comandado -> vet_comand
# em cima eu mudei aquelas variaveis por causa do flake8

from typing import List, Tuple


# codigo principal:
def main() -> None:
    vet = str_pra_int(input().split(','))
    while True:
        comando = input().split()
        if comando[0] == 'fim':
            break
        elif comando[0] == 'soma_elementos':
            b = soma_elementos(vet)
            vet.clear()
            vet.append(b)
            print(vet)
        else:
            vet_comando = str_pra_int(input().split(','))
            if comando[0] == 'soma_vetores':
                soma_vetores(vet, vet_comando)
                print(vet)
            elif comando[0] == 'subtrai_vetores':
                subtrai_vetores(vet, vet_comando)
                print(vet)
            elif comando[0] == 'multiplica_vetores':
                multiplica_vetores(vet, vet_comando)
                print(vet)
            elif comando[0] == 'divide_vetores':
                divide_vetores(vet, vet_comando)
                print(vet)
            elif comando[0] == 'multiplicacao_escalar':
                multiplicacao_escalar(vet, vet_comando[0])
                print(vet)
            elif comando[0] == 'n_duplicacao':
                n_duplicacao(vet, vet_comando[0])
                print(vet)
            elif comando[0] == 'produto_interno':
                a = produto_interno(vet, vet_comando)
                vet.clear()
                vet.append(a)
                print(vet)
            elif comando[0] == 'multiplica_todos':
                multiplica_todos(vet, vet_comando)
                print(vet)
            elif comando[0] == 'correlacao_cruzada':
                correlacao_cruzada(vet, vet_comando)
                print(vet)


# utilitários:
def str_pra_int(L: List[str]) -> List[int]:
    if len(L) == 1 and L[0] == '':
        temp = []
        for i in range(len(L)):
            temp.append(int(L[i]))
        temp.clear
        return temp
    else:
        temp = []
        for i in range(len(L)):
            temp.append(int(L[i]))
        return temp


def poe_zero(vet: List[int], L: List[int]) -> Tuple[List[int], List[int]]:
    if len(vet) > len(L):
        i = len(vet) - len(L)
        while i != 0:
            L.append(0)
            i -= 1
    elif len(vet) < len(L):
        i = len(L) - len(vet)
        while i != 0:
            vet.append(0)
            i -= 1
    return L, vet


def poe_um(vet: List[int], L: List[int]) -> Tuple[List[int], List[int]]:
    if len(vet) > len(L):
        i = len(vet) - len(L)
        while i != 0:
            L.append(1)
            i -= 1
    elif len(vet) < len(L):
        i = len(L) - len(vet)
        while i != 0:
            vet.append(1)
            i -= 1
    return L, vet


# funções:
def soma_vetores(vet: List[int], vet_comand: List[int]) -> List[int]:
    poe_zero(vet, vet_comand)
    for i in range(len(vet)):
        vet[i] = vet[i] + vet_comand[i]
    return vet


def subtrai_vetores(vet: List[int], vet_comand: List[int]) -> List[int]:
    poe_zero(vet, vet_comand)
    for i in range(len(vet)):
        vet[i] = vet[i] - vet_comand[i]
    return vet


def multiplica_vetores(vet: List[int], vet_comand: List[int]) -> List[int]:
    poe_um(vet, vet_comand)
    for i in range(len(vet)):
        vet[i] = vet[i] * vet_comand[i]
    return vet


def divide_vetores(vet: List[int], vet_comand: List[int]) -> List[int]:
    if len(vet) < len(vet_comand):
        poe_zero(vet, vet_comand)
    elif len(vet) > len(vet_comand):
        poe_um(vet, vet_comand)
    for i in range(len(vet)):
        vet[i] = vet[i] // vet_comand[i]
    return vet


def multiplicacao_escalar(vet: List[int], n: int) -> List[int]:
    for i in range(len(vet)):
        vet[i] = vet[i] * n  # não é L de um termo, um numero
    return vet


def n_duplicacao(vet: List[int], n: int) -> List[int]:
    if n == 0:
        vet = []
        return vet
    else:
        temp = vet[:]
        i = 1
        while i < n:
            vet.extend(temp)
            i += 1
        return vet


def soma_elementos(vet: List[int]) -> int:
    if vet == []:
        return 0
    else:
        soma = vet[0]
        for i in range(len(vet)-1):
            soma += vet[i+1]
        return soma


def produto_interno(vet: List[int], vet_comand: List[int]) -> int:
    if vet_comand == [] and vet == []:
        return 0
    else:
        poe_um(vet, vet_comand)
        temp = []
        for i in range(len(vet)):
            temp.append(vet[i] * vet_comand[i])
        return soma_elementos(temp)


def multiplica_todos(vet: List[int], vet_comand: List[int]) -> List[int]:
    if vet_comand == []:
        poe_zero(vet_comand, vet)
    resultado = []
    for i in range(len(vet)):
        temp = []
        for j in range(len(vet_comand)):
            temp.append(vet[i]*vet_comand[j])
        resultado.append(soma_elementos(temp))
    vet.clear()
    vet.extend(resultado)
    return vet


def correlacao_cruzada(vet: List[int], vet_comand: List[int]) -> List[int]:
    i = 0
    temp = []
    while i < (len(vet)-(len(vet_comand)-1)):
        temp2 = vet[i:len(vet_comand)+i]
        temp.append(produto_interno(temp2, vet_comand))
        i += 1
    vet.clear()
    vet.extend(temp)
    return vet


# execução do código principal:
if __name__ == '__main__':
    main()

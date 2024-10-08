print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.") 
print("Seu SO anterior era Linux?","\n(0) Não","\n(1) Sim", sep="")
R1 = int(input()) #R = resposta; número = número da resposta
if(R1 == 0): #primeira separação (não)
    print("Seu SO anterior era um MacOS?", "\n(0) Não", "\n(1) Sim", sep="")
    R2 = int(input())
    if(R2 == 0):
      print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro.", sep="")  
    elif(R2 == 1): print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS.", sep="")
    else: print("Opção inválida, recomece o questionário.")
elif(R1 == 1): #primeira separação (sim)
    print("É programador/ desenvolvedor ou de áreas semelhantes?", "\n(0) Não", "\n(1) Sim", "\n(2) Sim, realizo testes e invasão de sistemas", sep="")
    R2 = int(input())
    if(R2 == 0): 
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora.", sep="")
    elif(R2 == 2):
        print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch.", sep="")
    elif(R2 == 1): #caso do meio (mais possibilidades)
        print("Gostaria de algo pronto para uso ao invés de ficar configurando o SO?", "\n(0) Não", "\n(1) Sim", sep="")
        R3 = int(input())
        if(R3 == 0): 
            print("Já utilizou Arch Linux?", "\n(0) Não", "\n(1) Sim", sep="")
            R4 = int(input())
            if(R4 == 0): 
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux.", sep="")
            elif(R4 == 1): print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware.", sep="")
            else: print("Opção inválida, recomece o questionário.")
        elif(R3 == 1):
            print("Já utilizou Debian ou Ubuntu?", "\n(0) Não", "\n(1) Sim", sep="")
            R4 = int(input())
            if(R4 == 0):
                print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu.", sep="")
            elif(R4 == 1): print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS.", sep="")
            else: print("Opção inválida, recomece o questionário.")
        else: print("Opção inválida, recomece o questionário.")
else: print("Opção inválida, recomece o questionário.")
S = input() #Jogada de Sheila, if wins => Interestelar
R = input() #Jogada de Reginaldo, if wins => Jornada nas Estrelas

# pedra papel tesoura lagarto spock

if ((S == "pedra" and R == "tesoura") or (S == "pedra" and R == "lagarto") or 
    (S == "papel" and R == "spock") or (S == "papel" and R == "pedra") or 
    (S == "tesoura" and R == "papel") or (S == "tesoura" and R == "lagarto") or 
    (S == "lagarto" and R == "spock") or (S == "lagarto" and R == "papel") or 
    (S == "spock" and R == "tesoura") or (S == "spock" and R == "pedra")):
    print("Interestelar")  
elif (S == R):
    print("empate")
else:
    print("Jornada nas Estrelas")
    
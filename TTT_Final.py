case = [
        "1","2","3",
        "4","5","6",
        "7","8","9",
        ]
symbol = "X"
restart = "o"
counter = 1
def tab(case):
    espace="|         |         |         |"
    ligne="+---------+---------+---------+"
    print(ligne)
    for i in range(0,7,3):
        print(espace)
        print(f"|    {case[i]}    |    {case[i+1]}    |    {case[i+2]}    |")
        print(espace)
        print(ligne)
def winner(case):
    if case[0]+case[1]+case[2]=="XXX" or case[3]+case[4]+case[5]=="XXX"\
        or case[6]+case[7]+case[8]=="XXX":
        print("X a gagné.")
    elif case[0]+case[1]+case[2]=="OOO" or case[3]+case[4]+case[5]=="OOO"\
        or case[6]+case[7]+case[8]=="OOO":
        print("O a gagné.")
    elif case[0]+case[3]+case[6]=="XXX" or case[1]+case[4]+case[7]=="XXX"\
        or case[2]+case[5]+case[8]=="XXX":
        print("X a gagné.")
    elif case[0]+case[3]+case[6]=="OOO" or case[1]+case[4]+case[7]=="OOO"\
        or case[2]+case[5]+case[8]=="OOO":
        print("O a gagné.")
    elif case[0]+case[4]+case[8]=="XXX" or case[2]+case[4]+case[6]=="XXX":
        print("X a gagné.")
    elif case[0]+case[4]+case[8]=="OOO" or case[2]+case[4]+case[6]=="OOO":
        print("O a gagné.")
    else:
        return False
def again(restart):
    restart=input("Continuer ? (O/N) : ")
    if restart=="n" or restart=="N":
        return restart
    elif restart=="o" or restart=="O":
        return restart     
    else:
        while restart!="o" or restart!="O" or restart!="n" or restart!="N":
            restart=input("Erreur... Continuer ? (O/N) : ")
            if restart=="o" or restart=="O":
                return restart
            elif restart=="n" or restart=="N":
                return restart    
def reset(restart,case,symbol,counter):
    if restart=="o" or restart=="O":
        print("On recommence.")
    case=["1","2","3",
          "4","5","6",
          "7","8","9"]
    symbol="X"
    counter+=1
    return case,symbol,counter

number = input("1 ou 2 joueurs : ")
while restart!="n" and restart!="N":
    if number=="2":
        print(f"Partie {counter}.")
        tab(case)
        for i in range(9):
            select = int(input(f"{symbol}, choisissez une case sur laquelle jouer : "))
            if select>9 or case[select-1]=="X" or case[select-1]=="O":
                while True:
                    if select>9 or case[select-1]=="X" or case[select-1]=="O":
                        select=int(input(f"Mauvaise case... {symbol}, rejouez : "))
                    elif symbol=="X":
                        case[select-1] = "X"
                        symbol = "O"
                        break
                    elif symbol=="O":
                        case[select-1] = "O"
                        symbol = "X"
                        break
            elif symbol=="O" and case[select-1]!="X" and case[select-1]!="O":
                case[select-1] = "O"
                symbol = "X"
            elif symbol=="X" and case[select-1]!="X" and case[select-1]!="O":
                case[select-1] = "X"
                symbol = "O"
            tab(case)
            if winner(case)!=False:
                break
            elif i==8:
                print("Match nul.")
        restart=again(restart)
        case,symbol,counter=reset(restart,case,symbol,counter)
    elif number=="1":
        print(f"Partie {counter}.")
        tab(case)
        for i in range(5):
            select = int(input("X, choisissez une case sur laquelle jouer : "))
            if select>9 or case[select-1]=="X" or case[select-1]=="O":
                while True:
                    if select>9 or case[select-1]=="X" or case[select-1]=="O":
                        select = int(input("Mauvaise case... X, rejouez : "))
                    else:
                        case[select-1] = "X"
                        break
            else:
                case[select-1] = "X"
            tab(case)
            if winner(case)!=False:
                break
            elif i==4:
                print("Match nul.")
            if counter%2==0:
                while True:
                    #Forêt d'if droit devant
                    if case[1]==case[2] or case[3]==case[6] or case[4]==case[8]:
                        if case[0]=="1":
                            case[0] = "O"
                            break           
                    if case[0]==case[2] or case[4]==case[7]:
                        if case[1]=="2":
                            case[1] = "O"
                            break
                    if case[0]==case[1] or case[5]==case[8] or case[4]==case[6]:
                        if case[2]=="3":
                            case[2] = "O"
                            break
                    if case[0]==case[6] or case[4]==case[5]:
                        if case[3]=="4":
                            case[3] = "O"
                            break
                    if case[3]==case[4] or case[2]==case[8]:
                        if case[5]=="6":
                            case[5] = "O"
                            break
                    if case[2]==case[4] or case[0]==case[3] or case[7]==case[8]:
                        if case[6]=="7":
                            case[6] = "O"
                            break
                    if case[1]==case[4] or case[6]==case[8]:
                        if case[7]=="8":
                            case[7] = "O"
                            break
                    if case[0]==case[4] or case[2]==case[5] or case[6]==case[7]:
                        if case[8]=="9":
                            case[8] = "O"
                            break
                    if case[4]=="5":
                        case[4] = "O"
                        break
                    if case[1]=="2":
                        case[1] = "O"
                        break
                    if case[3]=="4":
                        case[3] = "O"
                        break
                    if case[5]=="6":
                        case[5] = "O"
                        break
                    if case[7]=="8":
                        case[7] = "O"
                        break
                    if case[0]=="1":
                        case[0] = "O"
                        break
                    if case[2]=="3":
                        case[2] = "O"
                        break
                    if case[6]=="7":
                        case[6] = "O"
                        break
                    if case[8]=="9":
                        case[8] = "O"
                        break
                    else:
                        break
                tab(case)               
                if winner(case)!=False:
                    break
                elif i==4:
                    print("Match nul.")
            else:
                for j in range(9):
                    if case[j]!="X" and case[j]!="O":
                        case[j] = "O"
                        tab(case)
                        print(f"O a joué en case {j+1}.")
                        break                
                if winner(case)!=False:
                    break
                elif i==4:
                    print("Match nul.")
        restart=again(restart)
        case,symbol,counter=reset(restart,case,symbol,counter)
    else:
        number=input("Erreur... 1 ou 2 joueurs : ")


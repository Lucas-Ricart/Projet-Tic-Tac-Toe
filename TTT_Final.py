case = [                                                                                #liste, numéro des cases, sera modifié pour afficher les X et O joués
        "1","2","3",
        "4","5","6",
        "7","8","9",
        ]                                                                       
symbol = "X"                                                                            #variable pour l'affichage du joueur
restart = "o"                                                                           #variable pour continuer à jouer ou sortir de la boucle principale
counter = 1                                                                             #compteur de partie
def tab(case):                                                                          #fonction tab, affichage du plateau de jeu
    espace="|         |         |         |"
    ligne="+---------+---------+---------+"
    print(ligne)
    for i in range(0,7,3):                                                              #incrémentation de 3 pour que case soit bien placé
        print(espace)
        print(f"|    {case[i]}    |    {case[i+1]}    |    {case[i+2]}    |")
        print(espace)
        print(ligne)
def winner(case):                                                                       #fonction winner, vérifie les conditions de victoire
    if case[0]+case[1]+case[2]=="XXX" or case[3]+case[4]+case[5]=="XXX"\
        or case[6]+case[7]+case[8]=="XXX":                                              #condition X victoire ligne
        print("X a gagné.")
    elif case[0]+case[1]+case[2]=="OOO" or case[3]+case[4]+case[5]=="OOO"\
        or case[6]+case[7]+case[8]=="OOO":                                              #condition O victoire ligne
        print("O a gagné.")
    elif case[0]+case[3]+case[6]=="XXX" or case[1]+case[4]+case[7]=="XXX"\
        or case[2]+case[5]+case[8]=="XXX":                                              #condition X victoire colonne
        print("X a gagné.")
    elif case[0]+case[3]+case[6]=="OOO" or case[1]+case[4]+case[7]=="OOO"\
        or case[2]+case[5]+case[8]=="OOO":                                              #condition O victoire colonne
        print("O a gagné.")
    elif case[0]+case[4]+case[8]=="XXX" or case[2]+case[4]+case[6]=="XXX":              #condition X victoire diagonale
        print("X a gagné.")
    elif case[0]+case[4]+case[8]=="OOO" or case[2]+case[4]+case[6]=="OOO":              #condition O victoire diagonale
        print("O a gagné.")
    else:
        return False                                                                    #renvoi faux si pas de victoire
def again(restart):                                                                     #fonction again, demande si on relance une partie et renvoi restart en fonction
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
def reset(restart,case,symbol,counter):                                                 #fonction reset, renvoi case et symbol au valeurs d'origine pour recommencer une partie et incrémente le compteur du nombre de partie
    if restart=="o" or restart=="O":
        print("On recommence.")
    case=["1","2","3",
          "4","5","6",
          "7","8","9"]
    symbol="X"
    counter+=1
    return case,symbol,counter

number = input("1 ou 2 joueurs : ")                                                     #demande le nombre de joueur
while restart!="n" and restart!="N":                                                    #boucle principale
    if number=="2":                                                                     #mode de jeu 2 joueurs
        print(f"Partie {counter}.")                                                     #affiche le nombre de partie
        tab(case)                                                                       #affiche le plateau
        for i in range(9):                                                              #boucle, sortie en cas de victoire ou après 9 'passages'
            select = int(input(f"{symbol}, choisissez une case sur laquelle jouer : ")) #joueur donné par symbol, choisi la case où il veut jouer
            if select>9 or case[select-1]=="X" or case[select-1]=="O":                  #si entrée pas ok et case pas dispo alors
                while True:                                                             #boucle pour avoir une bonne entrée
                    if select>9 or case[select-1]=="X" or case[select-1]=="O":          #si toujours pas ok
                        select=int(input(f"Mauvaise case... {symbol}, rejouez : "))     #demande case de jeu
                    elif symbol=="X":                                                   #si ok et tour de X
                        case[select-1] = "X"                                            #met X sur la case selectionné
                        symbol = "O"                                                    #passe au joueur O
                        break                                                           #sortie boucle, entrée ok
                    elif symbol=="O":                                                   #si ok et tour de O
                        case[select-1] = "O"                                            #met O sur la case selectionné
                        symbol = "X"                                                    #passe au joueur X
                        break                                                           #sortie boucle, entrée ok
            elif symbol=="O":                                                           #si tour de O 
                case[select-1] = "O"                                                    #met O sur la case
                symbol = "X"                                                            #passe au joueur X
            elif symbol=="X":                                                           #si tour de X
                case[select-1] = "X"                                                    #met X sur la case
                symbol = "O"                                                            #passe au joueur O
            tab(case)                                                                   #affiche plateau
            if winner(case)!=False:                                                     #appel et test la fonction winner, si pas de victoire
                break                                                                   #ne sort pas de la boucle l69
            elif i==8:                                                                  #sinon si i=8 toutes les cases sont pleines, alors
                print("Match nul.")                                                     #match nul
        restart=again(restart)                                                          #demande si on recommence et met restart à jour en concéquence
        case,symbol,counter=reset(restart,case,symbol,counter)                          #appel reset pour mettre à zéro les cases et le joueur et incrémenter le compteur du nombre de partie
    elif number=="1":                                                                   #mode de jeu solo
        print(f"Partie {counter}.")                                                     #affiche nombre de partie
        tab(case)                                                                       #affiche plateau
        for i in range(5):                                                              #boucle, sortie en cas de victoire ou après 5 'passages'
            select = int(input("X, choisissez une case sur laquelle jouer : "))         #le joueur choisi une case
            if select>9 or case[select-1]=="X" or case[select-1]=="O":                  #vérification entrée
                while True:                                                             #same
                    if select>9 or case[select-1]=="X" or case[select-1]=="O":
                        select = int(input("Mauvaise case... X, rejouez : "))           #same
                    else:                                                               
                        case[select-1] = "X"
                        break                                                           #but
            else:
                case[select-1] = "X"                                                    #different
            tab(case)                                                                   #affiche le plateau
            if winner(case)!=False:                                                     #test victoire
                break
            elif i==4:                                                                  #test match nul, fini en 4 'passages' dans la boucle
                print("Match nul.")
            if counter%2==0:                                                            #bot 1 partie /2
                while True:                                                             #boucle pour le bot cherche où placer O
                    #Forêt d'if droit devant
                    #pour vérifier un paquet de condition pour jouer O
                    #et éviter de placer plusieurs O
                    #ou ne pas en placer du tout
                    if case[1]==case[2] or case[3]==case[6] or case[4]==case[8]:        #test 1 condition
                        if case[0]=="1":                                                #vérifie que la case cible est libre
                            case[0] = "O"                                               #si ok place O
                            break                                                       #sort de la boucle pour ne pas passer à d'autres if
                    if case[0]==case[2] or case[4]==case[7]:                            #si précédent pas ok test tout les if
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
                        break                                                           #pour sortir de la boucle en cas de match nul           
                tab(case)                                                               #affiche plateau
                print(f"O a joué en case {j+1}.")                                       #affiche la case du nouveau O
                if winner(case)!=False:                                                 #test victoire
                    break
                elif i==4:                                                              #test nul
                    print("Match nul.")
            else:                                                                       #parties impaires
                for j in range(9):                                                      #boucle pour défiler les cases de 1 à 9
                    if case[j]!="X" and case[j]!="O":                                   #test case libre
                        case[j] = "O"                                                   #si oui place O
                        tab(case)                                                       #affiche plateau
                        print(f"O a joué en case {j+1}.")                               #indique case O
                        break                                                           #sortie boucle
                if winner(case)!=False:                                                 #test victoire
                    break
                elif i==4:                                                              #test match nul
                    print("Match nul.")
        restart=again(restart)                                                          #on recommence ?
        case,symbol,counter=reset(restart,case,symbol,counter)                          #plateau, joueur et compteur à jour
    else:                                                                               #si mauvaise selection du nombre de joueur
        number=input("Erreur... 1 ou 2 joueurs : ")                                     #redemande une entrée du nombre de joueur
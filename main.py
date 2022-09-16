# mini projet
from random import randint

def Fast_Overarm():
    """resumé
    choisi une varible aleatoire et la renvoie

    Returns:
        int: un entier representen les points 
    """
    random = randint(0,100)
    if random <= 50:
        return 0
    if  51 <= random <= 55:
        return 20
    if 56 <= random <= 65:
       return 30
    if 66 <= random <= 100:
        return 40
    

def Controlled_overarm() :
    """resumé
    choisi une varible aleatoire et la renvoie

    Returns:
        int: un entier representen les points 
    """
    random = randint(0,101)
    if random == 0:
        return 0 
    if 1 <= random <= 42:
        return 10
    if 43 <= random <= 77:
        return 20
    if 78 <= random <= 100:
        return 30
    if random == 101 :
        return 40

def Underarm():
    """resumé
    choisi une varible aleatoire et la renvoie

    Returns:
        int: un entier representen les points 
    """
    random = randint(0,100)
    if random <= 5:
       return 0
    if 6 <= random <= 46:
       return 10
    if 47 <= random <= 77:
        return 20
    if 78 <= random <= 98:
        return 30
    if random >= 99:
        return 40
    

def couleur(r, g, b, texte):
    """resumée 
       prend une valeur rgb et un texte et le met en couleur 
    
    parametre:
        r (int): nombre de rouge
        g (int): nombre de vert
        b (int): nombre de bleu
        texte (str):  texte en str

    Returns:
        str: le texte en couleur
    """
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, texte)

def mode_de_tire():
    """resumé
    demande a l'utilisateur un nombre entier de 1 a 3 
    pour selectiner un mode de tir parmis les 3 fonction definit precedaments 
    et qui gere les entrer utilisateur 

    Returns:
        int: les points a ajoutez aux joueur actuel
    """
    demande = ""
    while True:
        while not demande.isdigit():
            print(couleur(135,206,235,"quel mode voulez vous ?\n \n Fast_Overarm [1] \n Controlled_overarm [2] \n Underarm[3]"))
            
            demande = input(couleur(0,100,0,"==>"))
            #print(couleur(255,0,0,"\nchosis un nombre entier  entre 1 et 3 inclus\n"))   
        demande = int(demande)
          
        if demande == 1:
                score = Fast_Overarm()
                break
        if demande == 2:
                score = Controlled_overarm()
                break
        if demande == 3:
            score = Underarm()
            break
        else:
            #print(couleur(255,0,0,"\nchosis un nombre entier  entre 1 et 3 inclus\n"))
            print(couleur(135,206,235,"quel mode voulez vous ? \n \
                        Fast_Overarm [1] \n \
                        Controlled_overarm [2]\n \
                        Underarm[3]"))
            demande = input(couleur(0,100,0,"==>"))
            
    return score

mode_de_tire()



    

    





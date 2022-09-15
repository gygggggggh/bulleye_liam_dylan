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
    

    

    





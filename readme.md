# projet bulleye

![alt text]([https://img.freepik.com/premium-vector/letter-b-bullseye-logo-vector-template_138551-150.jpg?w=740](https://img.freepik.com/free-vector/hand-holding-dart-close-target-person-with-idea-goal-aim-flat-vector-illustration-motivation-marketing-challenge-success-concept-banner-website-design-landing-web-page_74855-26010.jpg?w=996&t=st=1663182662~exp=1663183262~hmac=16e9fcd78caec319f132ca8085c2a059950a579e0ab4823eed64cf4e06a9caf6))

## probleme

### les type de donnés

- afficher le score a chaque fois
- demander le nombre de joueur -> score en dico

```python

{
  "dylan": "20",
  "schertzer": "180",
}
```

- une liste qui pour le nom des joueur : utilise l'index pour le noms

```python
0     1
[dylan,liam]
```

### l'aleatoire

- la fonction randint de convient pas a cette situation
- nous avont donc deconvert la fonction random.choices
comme montrez ci dessous

```python
from random import choices

point = 0,10,20,30,40
for i in range(100):
    test = (choices(point , weights= (50,0,5,10,35)))#Fast Overarm 
    print(f'vous avez gagner {test} point')

```

## les fonction

- une fonction tir
avec 3 condition
les 3 mode de tirs

## la boucle de jeu

```python
def boucle principale():
    affiche le joueur qui joue  avec "tour de x"
    pour chaque joueur
        demande un mode de tirs
        execute la fonction tirs
        ajoute le score dans le dico
    affiche manchee terminer
    regarde si un joueur a un score > 200
    si oui le jeu est finit : x a gagner avec xxx points
    sinon affiche manche suivante
```

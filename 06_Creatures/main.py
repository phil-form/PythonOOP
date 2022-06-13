from random import randint, random, randrange
from Models.Creatures import Creature
from Models.Dresseurs import Dresseur

d1 = Dresseur("Riri")
d1.ajouterCreature(Creature("Machin", 15, 10, 5, 1))
d1.ajouterCreature(Creature("Truc", 18, 6, 10, 2))
d1.ajouterCreature(Creature("Brole", 30, 1, 1, 10))

d2 = Dresseur("Loulou")
d2.ajouterCreature(Creature("Samsung", 15, 10, 5, 1))
d2.ajouterCreature(Creature("Apple", 18, 6, 10, 2))
d2.ajouterCreature(Creature("Microsftatchu", 30, 1, 1, 10))

d1.debutMatch()
d2.debutMatch()

print("Le combat commence!")

print(d1.activeCreature)
print(d2.activeCreature)
print()

def choisirCreature(dresseur: Dresseur):
    terminer = False
    while not terminer:
        position = randrange(0, dresseur.nbCreature)
        terminer = dresseur.changerCreature(position)

def manageChoix(dresseur: Dresseur):
    # 0 changer 1 esquive 2 se proteger 3 attaquer
    choix = randrange(0, 4)

    if choix == 0 and not dresseur.estVaincu:
        choisirCreature(dresseur)
    elif choix == 1:
        dresseur.ordreEsquive()
    elif choix == 2:
        dresseur.ordreDefense()
    
    return choix

while not(d1.estVaincu or d2.estVaincu):
    choix1 = manageChoix(d1)
    choix2 = manageChoix(d2)

    if choix1 == 3 and choix2 == 3:
        print("D1 et D2 attaquent")

        if d1.activeCreature.vitesse > d2.activeCreature.vitesse:
            d_ini = d1
            d_sec = d2
        elif d1.activeCreature.vitesse == d2.activeCreature.vitesse:
            if randint(1, 2) == 1:
                d_ini = d1
                d_sec = d2
            else:
                d_ini = d2
                d_sec = d1
        else:
            d_ini = d2
            d_sec = d1

        d_ini.ordreAttaquer(d_sec.activeCreature)

        if not d_sec.activeCreature.estKo:
            d_sec.ordreAttaquer(d_ini.activeCreature)

    elif choix1 == 3:
        print(f"{d1} attaque")
        d1.ordreAttaquer(d2.activeCreature)
    elif choix2 == 3:
        print(f"{d2} attaque")
        d2.ordreAttaquer(d1.activeCreature)

    if (not d1.estVaincu and d1.activeCreature.estKo):
        choisirCreature(d1)
        print("d1 ko -> swich")

    if (not d2.estVaincu and d2.activeCreature.estKo):
        choisirCreature(d2)
        print("d1 ko -> swich")

    print("Fin de tour")
    print(d1.activeCreature)
    print(d2.activeCreature)
    print()

d1.terminerMatch()
d2.terminerMatch()

if not d1.estVaincu:
    print(f"{d1} a gagné")
else:
    print(f"{d2} a gagné")
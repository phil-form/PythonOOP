from Models.Personnage import Personnage
from Models.Humain     import Humain
from Models.Nain       import Nain
from Models.Monstre    import Monstre
from Models.Loup       import Loup
from Models.Orque      import Orque
from Models.Dragonnet  import Dragonnet

from Models.Des        import Des

## choix du héros
de2 = Des(1, 2)     ## pour choisir entre humain (1) et nain (2)
if de2.lance() == 1:
    heros = Humain()
else:
    heros = Nain()

print("Héros:")
print("  ", heros)

## choix des 10 monstres
de3 = Des(1, 3)     ## pour choisir entre loup (1), orque (2) et dragonnet (3)
monstre = []
for i in range(10):
    m = de3.lance()
    if m == 1:
        mm = Loup()
    elif m == 2:
        mm = Orque()
    else:
        mm = Dragonnet()
    monstre.insert(i, mm)

print("Monstres:")
n = 0
for mm in monstre:
    n += 1
    print(f"  {n} ", mm)

## combat(s)
hm = 1 ## 1 = heros, 2 = monstre
m = Monstre.next(monstre)   ## je choisis 1 monstre au hasard parmi les 10
while (heros.curV > 0) and (Monstre.alives(monstre) > 0):   ## tant que le héros est vivant
                                                            ## et qu'il reste au moins 1 PV à l'ensemble de tous les mosntres 
    if hm == 1:                         ## c'est au héros de frapper
        heros.frappe(monstre[m])
        if monstre[m].curV <= 0:        ## ce monstre est mort:
            m = Monstre.next(monstre)   ##      j'en choisis un autre
            heros.curV = heros.pv       ##      je restaure les points de vie du héros
            hm = 2                      ##      je donne la main au monstre, pour que le héros la récupère

    else:                               ## c'est au monstre de frapper
        monstre[m].frappe(heros)

    hm = 3 - hm                         ## la main passe

## combat terminé
if heros.curV == 0:
    print("Le héros a perdu ...")
else:
    print("Le héros a gagné !!!")
print("Héros:")
print("  ", heros)
print("Monstres:")
n = 0
for mm in monstre:
    n += 1
    print(f"  {n} ", mm)

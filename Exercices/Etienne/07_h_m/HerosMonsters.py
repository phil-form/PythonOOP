from Models.Personnage import Personnage
from Models.Humain     import Humain
from Models.Nain       import Nain
from Models.Monstre    import Monstre
from Models.Loup       import Loup
from Models.Orque      import Orque
from Models.Dragonnet  import Dragonnet

from Models.Des        import Des
import os

class Plateau:
    def __init__(self, nx: int, ny: int, nm: int):
        self.__nx  = nx
        self.__ny  = ny
        self.cases = self.__prep()
        self.mm    = self.__emptyMm(nm)
        self.__adv = -1

    @property
    def nx(self):
        return self.__nx

    @nx.setter
    def nx(self, v: int):
        self.__nx = v

    @property
    def ny(self):
        return self.__ny

    @ny.setter
    def ny(self, v: int):
        self.__ny = v

    @property
    def cases(self):
        return self.__cases

    @cases.setter
    def cases(self, v):
        self.__cases = v

    @property
    def adv(self):
        return self.__adv

    @adv.setter
    def adv(self, v: int):
        self.__adv = v

    def __prep(self):
        t = []
        for i in range(0, self.ny):
            l = []
            for j in range(0, self.nx):
                l.insert(j, -99)
            t.insert(i, l)
        return t

    def __emptyMm(self, nm: int):
        mm = []
        for i in range(0, nm):
            mm.insert(i, Humain(0, 0))
        return mm

    ## vérifie s'il y a un monstre à moins de d cases de la position donnée
    ## renvoie 1 si trouvé au-dessus
    ##         2 si trouvé à droite
    ##         3 si trouvé en-dessous
    ##         4 si trouvé à gauche
    ##        -1 si pas trouvé
    def voisin(self, d: int, x: int, y: int) -> int:
        ## on va balayer un carré allant de notre position -d à +d ... si on n'est pas en-dehors du plateau
        x0 = x - d              ## x from
        if x0 < 0:              ## pas moions de 0
            x0 = 0
        x1 = x + d              ## x to
        if x1 >= self.nx:       ## pas plus de nx
            x1 = self.nx - 1
        y0 = y - d              ## y from
        if y0 < 0:              ## pas moins de 0
            y0 = 0
        y1 = y + d              ## y to
        if y1 >= self.ny:       ## pas plus de ny
            y1 = self.ny - 1

        ## on balaye
        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                if (i != x) or (j != y):        ## je ne me regarde pas moi-même ...
                    if (d > 1) or ((d == 1) and ((i == x) or (y == j))):
                        if  self.cases[j][i] >= 0:  ## -99: vide, -1: héros, 0 à ...: index d'un monstre
                            if j < y:               ## trouvé au-dessus
                                return 1
                            elif i > x:             ## trouvé à droite
                                return 2
                            elif j > y:             ## trouvé en-dessous
                                return 3
                            elif i < x:             ## trouvé à gauche
                                return 4
        return -1                               ## aucun voisin trouvé
    ## fin fonction voisin

    ## record a personnage in cases
    def setPers(self, p: Personnage):
        n = -2
        if p.pers < 20: ## hero: set -1 in cases
            n = -1
        else:           ## monstre: set is number in monster array in cases
            for i in range(0, len(self.mm)):
                if (self.mm[i].x == p.x) and (self.mm[i].y == p.y): ## found by position
                    n = i
        self.cases[p.y][p.x] = n
    ## fin méthode setPers

    ## dessine le tableau complet
    def __str__(self):
        if self.adv == -1:
            x = -1
            y = -1
        else:
            x = self.mm[self.adv].x
            y = self.mm[self.adv].y
        t = '+-'
        for j in range(0, self.nx):
            t += "--"
        t += '+\n'
        for i in range(0, self.ny):
            l = '| '
            for j in range(0, self.nx):
                if self.cases[i][j] == -99:     ## empty
                    l = l + '  '
                elif self.cases[i][j] == -1:    ## heros
                    l = l + 'H '
                elif self.cases[i][j] == -2:    ## monstre inconnu
                    l = l + '? '
                elif self.cases[i][j] >= 0:     ## monstre
                    if False: ## for debug: true = debug (always show all monsters), false = normal (show only current)
                        s = self.mm[self.cases[i][j]].nom()
                    else:
                        if (x == j) and (y == i):   ## l'adversaire courant
                            s = self.mm[self.cases[i][j]].nom()
                        else:
                            s = ' '
                    l = l + s[0] + ' '
            l += '|'
            t = t + l + "\n"
        t += '+-'
        for j in range(0, self.nx):
            t += "--"
        t += '+'
        return t

## fin class Plateau

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# #                                         # # # # # # # # # # # # # # # # # # # # # # # # # # #
# #   D E B U T   D U   P R O G R A M M E   # # # # # # # # # # # # # # # # # # # # # # # # # # #
# #                                         # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

os.system("clear")

sz = 15
nm = 10
mv = 10
pl = Plateau(sz, sz, nm)

## choix des 10 monstres
de3  = Des(1, 3)        ## pour choisir entre loup (1), orque (2) et dragonnet (3)
de15 = Des(0, sz - 1)   ## pour choisir une case dans le tableau

for i in range(nm):
    busy = True
    while busy:
        x = de15.lance()
        y = de15.lance()
        busy = (pl.voisin(2, x, y) != -1)
    m = de3.lance()
    if m == 1:
        mm = Loup(x, y)
    elif m == 2:
        mm = Orque(x, y)
    else:
        mm = Dragonnet(x, y)
    pl.mm[i] = mm
    pl.setPers(mm)

## choix du héros
de2 = Des(1, 2)     ## pour choisir entre humain (1) et nain (2)
busy = True
while busy:
    x = de15.lance()
    y = de15.lance()
    busy = (pl.voisin(1, x, y) != -1)
if de2.lance() == 1:
    heros = Humain(x, y)
else:
    heros = Nain(x, y)
pl.setPers(heros)

print("Héros:")
print("  ", heros)

## déplacements
msg = "" ## pour forcer un "enter" après l'affichage initial du héros
while msg != "fin":
    s = input(msg)
    if msg != "":
        s = s[0].lower()
        d = -1
        if (s == 'h') or (s == 'u'):                ## haut
            d = 1
        elif (s == 'd') or (s == 'r'):              ## droit
            d = 2
        elif (s == 'b') or (s == 'd'):              ## bas
            d = 3
        elif (s == 'g') or (s == 'l'):              ## gauche
            d = 4
        elif (s == '9'):
            msg = "fin"
        if d > -1:                                  ## direction valable
            x = heros.x                             ## pour l'effacer après de l'ancienne position
            y = heros.y
            if heros.move(d, sz, sz) > -1:          ## le déplacement était valide (pas en-dehors du plateau)
                pl.cases[y][x] = -99                ## efface l'ancienne position du héros
                pl.setPers(heros)                   ## le met à sa nouvelle place
                d = pl.voisin(1, heros.x, heros.y)
                if d > -1:                          ## il y a un monstre à côté
                    if d == 1:                      ## au-dessus
                        x = heros.x
                        y = heros.y - 1
                    elif d == 2:                    ## à droite
                        x = heros.x + 1
                        y = heros.y
                    elif d == 3:                    ## en-dessous
                        x = heros.x
                        y = heros.y + 1
                    elif d == 4:                    ## à gauche
                        x = heros.x - 1
                        y = heros.y

                    m = pl.cases[y][x]              ## numéro du monstre
                    pl.adv = m
                    os.system("clear")              ## redessine le plateau
                    print(pl)

                    ## bagare ...
                    input(f"H: {heros.x}-{heros.y}, M: {x}-{y} => {m}")
                    hm = 1 ## 1 = heros, 2 = monstre
                    while (heros.curV > 0) and (pl.mm[m].curV > 0):   ## tant que les 2 combattants sont vivants
                        if hm == 1:                     ## c'est au héros de frapper
                            heros.frappe(pl.mm[m])
                            if pl.mm[m].curV <= 0:      ## ce monstre est mort:
                                heros.curV = heros.pv   ##      je restaure les points de vie du héros

                        else:                           ## c'est au monstre de frapper
                            pl.mm[m].frappe(heros)

                        hm = 3 - hm                     ## la main passe

                    if heros.curV == 0:                 ## le héros est mort: fin du jeu
                        input("Le héros a perdu ...")
                        msg = "fin"
                    elif Monstre.alives(pl.mm) > 0:     ## il reste au moins un monstre en vie: on continue
                        print("Ce monstre est vaicnu:")
                        print(f"  {m} ", pl.mm[m])
                        mv -= 1
                        print(f"Il reste {mv} monstre(s) à combattre")
                        pl.cases[pl.mm[m].y][pl.mm[m].x] = -99
                        pl.adv = -1
                        input("")
                    else:                               ## tous les monstres sont morts: fin de partie
                        input("Le héros a gagné !!!" )
                        pl.cases[pl.mm[m].y][pl.mm[m].x] = -99
                        msg = "fin"

    if msg != "fin":
        msg = "\n[H]aut   / [U]p\n[D]roit  / [R]ight\n[B]as    / [B]ottom\n[G]auche / [L]eft\n\n 9 pour sortir\n\n   Votre choix: "
    os.system("clear")
    print(pl)

## combat terminé
os.system("clear")
print(pl)
print("")
if heros.curV == 0:                 ## le héros est mort: fin du jeu
    print("Le héros a perdu ...")
else:                               ## tous les monstres sont morts: fin de partie
    print("Le héros a gagné !!!" )
print("")
print("Héros:")
print("  ", heros)
print("Monstres:")
n = 0
for mm in pl.mm:
    n += 1
    print(f"  {n} ", mm)

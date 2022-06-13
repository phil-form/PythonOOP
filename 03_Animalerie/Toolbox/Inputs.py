from datetime import datetime
from multiprocessing.sharedctypes import Value

def readInt(msg):
    choice = 0
    while True:
        try:
            choice = int(input(msg))
        except ValueError:
            print("Entrer une valeur correcte!")
        else:
            return choice

def readStr(msg):
    return input(msg)

def readBool(msg):
    choice = 0
    while True:
        try:
            choice = int(input("Entrer 0 pour vrais, 1 pour false " + msg))
        except:
            print("Entrer 0 ou 1!")
        else:
            if choice == 1:
                return True
            elif choice == 0:
                return False
            else:
                print("Entrer 0 ou 1!")

def readDate(msg):
    choice = datetime.now()

    while True:
        try:
            choice = datetime.strptime(input(msg), "%d/%m/%y")
        except ValueError:
            print("Entrer une valeur correcte")
        else:
            return choice
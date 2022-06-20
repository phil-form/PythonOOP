class Coord:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def isGreaterObject(a, b, comp):
    return comp(a, b)

a = Coord(5, 7)
b = Coord(9, 4)

def compCoord(a: Coord, b: Coord):
    return a.x > b.x and a.y > b.y

print(isGreaterObject(a, b, compCoord))
print(isGreaterObject(a, b, lambda a, b : a.x > b.x and a.y > b.y))
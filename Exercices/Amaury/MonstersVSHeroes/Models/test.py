from Human import Human
from Dwarf import Dwarf
from Wolf import Wolf
from Dragon import Dragon
from Goblin import Goblin


human = Human()
dwarf = Dwarf()
wolf = Wolf()
dragon = Dragon()
goblin = Goblin()

print(f'Human force: {human.force}')
print(f'Dwarf force: {dwarf.force}')

print(f'Wolf ressource: gold: {wolf.gold}, leather: {wolf.leather}')
print(f'Dragon ressource: gold: {dragon.gold}, leather: {dragon.leather}')
print(f'Goblin ressource: gold: {goblin.gold}, leather: {goblin.leather}')
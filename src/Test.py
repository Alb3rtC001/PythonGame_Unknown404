import sys
sys.path.insert(0,"..")
from Module.Character import Personaje

new_character = Personaje("MrRobot", 100, 10, 1, 1, 1, 0, 1)
print(new_character.print_Stats())
print("funciona")

class Object:

    name = ""
    health = 1
    damage = 1
    dmg_properties = {"cortante": 0, "perforante": 0, "contundente": 0}
    range = 1
    weight = 1
    tech = 1 #Relacionado a si es algo primitivo/Versatil/Avanzado
    join = 0 #Ensamblar para un futuro

    def __init__(self, name, health, damage, dmg_properties, range, weight, tech, join):
        self.name = name
        self.health = health
        self.damage = damage
        self.dmg_properties = dmg_properties
        self.range = range
        self.weight = weight
        self.tech = tech
        self.join = join
        
    



class Personaje:

    #Atributos
    __name = "Pj"
    __health = 10
    __dmg = 1
    __defence = 10
    __speed = 1
    __atck_sp = 1
    __lucky = 1
    __intel = 1
    
    def __init__(self, name, health, dmg, defence, speed, atck_sp, lucky, intel):
        
        self.name = name or self.__name
        self.health = health or self.__health
        self.dmg = dmg or self.__dmg
        self.defence = defence or self.__defence
        self.speed = speed or self.__speed
        self.atck_sp = atck_sp or self.__atck_sp
        self.lucky = lucky or self.__lucky
        self.intel = intel or self.__intel

    def atack(self):
        pass

    def attack(self, damage):
        #Añadir la defence al dmg (O aplicar diferente planteamiento)
        return self.health  - damage if self.health - damage >= 0 else 0

    def move(self):
        pass

    def stats(self):
        #Devolver un JSON de las stats
        print("--------- ", self.name ," ----------")
        print("Health: ",self.health)
        print("Dmg: ",self.dmg)
        print("Def: ",self.defence)
        print("Vel: ",self.speed)
        print("Atc. Speed: ",self.atck_sp)
        print("Luck: ",self.lucky)
        print("Intel: ",self.intel)
        print("--------------------------")
    
    def dead(self):
        self.health = 0

    def is_alive(self):
        return self.health > 0
    
    def level_up(self, stat):
        pass

    #Atacar

    #Mover

    #Interactuar

    #Morir

    #Estadisticas

    #Robot -> Reparar

class Personaje(object):

    #Atributos
    __vida = 10
    __daño = 1
    __defensa = 10
    __velocidad = 1
    __vel_atck = 1
    __suerte = 1
    __intel = 1
    
    def __init__(self, vida, daño, defensa, velocidad, vel_atck, suerte, intel):
        
        self.vida = vida or self.__vida
        self.daño = daño or self.__daño
        self.defensa = defensa or self.__defensa
        self.velocidad = velocidad or self.__velocidad
        self.vel_atck = vel_atck or self.__vel_atck
        self.suerte = suerte or self.__suerte
        self.intel = intel or self.__intel

    def atack(self):
        pass

    def dmg(self, damage):
        #Añadir la defensa al daño (O aplicar diferente planteamiento)
        return self.vida  - damage if self.vida - damage >= 0 else 0

    def move(self):
        pass

    def estats(self):
        pass
    
    def dead(self):
        self.vida = 0

    def is_alive(self):
        return self.vida > 0
    
    def  level_up(self, stat):
        pass

    #Atacar

    #Mover

    #Interactuar

    #Morir

    #Estadisticas

    #Robot -> Reparar
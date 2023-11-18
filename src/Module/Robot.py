from Character import Personaje

class Robot(Personaje):

    def __init__(self, name, health, dmg, defence, speed, atck_sp, lucky, intel):
        #super()
        self.name = name or self.__name
        self.health = health or self.__health
        self.dmg = dmg or self.__dmg
        self.defence = defence or self.__defence
        self.speed = speed or self.__speed
        self.atck_sp = atck_sp or self.__atck_sp
        self.lucky = lucky or self.__lucky
        self.intel = intel or self.__intel


    pass
from enum import Enum

class tipo_movimiento(Enum):
    ataque=1
    defensa=0

class movimiento_general:
    def __init__(self,nombre,tipo,daño):
        self.nombre=nombre
        self.tipo=tipo
        self.daño=daño
    def get_nombre(self):
        return self.nombre
    def get_tipo(self):
        return self.tipo.name #hallar clave del enum(.value seria para sacar el valor)
    def get_daño(self):
        return self.daño
    def __str__(self):
        return f'el movimiento {self.nombre}'
class movimiento_especifico(movimiento_general):
    def __init__(self,nombre,tipo,daño,superheroe):
        super().__init__(nombre,tipo,daño)
        self.superheroe = superheroe
    def get_superheroe(self):
        return self.superheroe





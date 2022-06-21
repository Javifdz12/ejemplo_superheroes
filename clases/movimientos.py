from enum import Enum

class tipo_movimiento(Enum):
    ataque=1
    defensa=0

class movimiento_general:
    def __init__(self,nombre,tipo,daño):
        if type(nombre)!=str:
            raise Exception("nombre debe ser str")
        else:
            self.nombre=nombre
        if type(tipo)!=tipo_movimiento:
            raise Exception("eso no es un tipo de movimiento")
        else:
            self.tipo=tipo
        if type(daño)!=int:
            raise Exception("daño debe ser un int")
        else:
            self.daño=daño
    def get_nombre(self):
        return self.nombre
    def get_tipo(self):
        return self.tipo
    def get_daño(self):
        return self.daño
    def __str__(self):
        return f'{self.nombre}:\n {self.daño} ptos de {self.tipo.name} '
class movimiento_especifico(movimiento_general):
    def __init__(self,nombre,tipo,daño,superheroe):
        super().__init__(nombre,tipo,daño)
        self.superheroe = superheroe
    def get_superheroe(self):
        return self.superheroe





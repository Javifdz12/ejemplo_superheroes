from enum import Enum
from clases.servivo import ser_vivo
from clases.escenarios import Escenario
import random

class tipo_superheroe(Enum):
    humano=1
    no_humano=0
    def de_nombre(a):
        a=a.lower()
        e=None
        for tp in tipo_superheroe:
            if tp.name==a:
                e=tp
        if type(e)!=tipo_superheroe:
            raise Exception("tipo incorrecto")
        return e
class superheroe(ser_vivo):
    def __init__(self,alias,identidad,tipo,esc):
        self.alias=alias
        self.identidad=identidad
        if type(tipo)!=tipo_superheroe:
            raise Exception("tipo de superheroe invalido")
        else:
            self.tipo=tipo
        if type(esc)!=Escenario:
            raise Exception("escenario no existe")
        else:
            self.esc=esc
        if tipo.name=="humano":
            self.parrilla_poderes=[random.randint(3,8),random.randint(1,7),random.randint(2,6),random.randint(2,6),random.randint(1,7),random.randint(1,8)]
        else:
            self.parrilla_poderes=[random.randint(4,7),random.randint(1,8),random.randint(1,8),random.randint(3,8),random.randint(1,8),random.randint(3,7)]
        self.movimientos=[]
        self.coste=(esc.get_monedas()/esc.get_num_superheroes())*(sum(self.parrilla_poderes)/30)
        self.energia=esc.get_energia_vital()*self.parrilla_poderes[3]

    def get_alias(self):
        return self.alias
    def get_tipo(self):
        return self.tipo
    def get_esc(self):
        return self.esc
    def get_movimientos(self):
        for i in range(len(self.movimientos)):
            print(f'{i} - {self.movimientos[i].__str__()}')
    def get_coste(self):
        return self.coste
    def get_energia(self):
        return self.energia
    def set_movimientos(self,x):
        for mov in x:
            if mov.get_tipo().name=="ataque":
                mov.set_daño((mov.get_daño()/10)*(0.8*self.parrilla_poderes[1] + 0.25*self.parrilla_poderes[2] + 0.75*self.parrilla_poderes[5] + self.parrilla_poderes[4]))
            else:
                mov.set_daño((mov.get_daño()/10)*(self.parrilla_poderes[0] + 0.75*self.parrilla_poderes[2] + 0.25*self.parrilla_poderes[5] + 0.2*self.parrilla_poderes[1]))
            self.movimientos.append(mov)
    def atacar(self,obj,mov):
        obj.energia=obj.energia-self.movimientos[mov].get_daño()
    def __str__(self):
        return f'{self.alias}, {self.tipo.name}, cuesta {self.coste} monedas, tiene {self.energia} ptos de energía y los siguientes movimientos:\n {self.get_movimientos()}'

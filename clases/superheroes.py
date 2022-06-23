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
    def __init__(self,id,alias,identidad,tipo,esc):
        self.ids=[]
        if type(id)== int and id not in self.ids:
            self.ids.append(id)
            self.id=id
        else:
            raise TypeError("variable incorrecta o ya existente")
        self.alias=alias
        self.__identidad=identidad
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
        movs=""
        for i in range(len(self.movimientos)):
            movs+=(f'{i} - {self.movimientos[i].__str__()}\n')
        return movs
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
    def fight_defensa(self,daño):
        self.energia=self.energia-daño
        if self.is_muerto:
            self.energia=0

    def fight_ataque(self,obj,mov):
        print(f'{self.alias} va a atacar a {obj.alias}')
        obj.fight_defensa(self.movimientos[mov].get_daño())
        print(f'A {obj.alias} le queda {obj.get_energia()}ptos de energia')

    def elegir_mov(self):
        print(f'{self.alias} tiene la opcion de usar:\n')
        print(self.get_movimientos())
        x=int(input())
        return x

    def __str__(self):
        return f'{self.alias},con id {self.id}, {self.tipo.name}, cuesta {self.coste} monedas, tiene {self.energia} ptos de energía y los siguientes movimientos:\n {self.get_movimientos()}'

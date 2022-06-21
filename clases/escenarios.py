from enum import Enum

class tipo_escenario(Enum):
    santo_santuario=[10000,10,10,100]
    torre_stark=[20000,20,25,200]
    colegio_xavier=[80000,30,40,300]

class Escenario:
    def __init__(self,monedas,num_superheroes,movimientos,energia_vital):
        self.monedas = monedas
        self.num_superheroes = num_superheroes
        self.movimientos = movimientos
        self.energia_vital =energia_vital
    def get_monedas(self):
        return self.monedas
    def get_num_superheroes(self):
        return self.num_superheroes
    def get_movimientos(self):
        return self.movimientos
    def get_energia_vital(self):
        return self.energia_vital
    def __str__(self):
        return f'monedas : {self.monedas}\nnum_superheroes : {self.num_superheroes}\nmovimientos : {self.movimientos}\nenergia_vital : {self.energia_vital}'

    def denombre(nom):
        x=nom.lower()
        esc=None
        for tp in tipo_escenario:
            if tp.name==x:
                a=tp.value
                esc=Escenario(a[0],a[1],a[2],a[3])

        if type(esc)!=Escenario:
            raise Exception("nombre no existe")
        return esc






class jugador:
    def __init__(self,nombre,equipo):
        self.nombre=nombre
        self.equipo=equipo
    def get_equipo(self):
        equip=""
        for i in range(len(self.equipo)):
            equip+=f'{i}- {self.equipo[i].__str__()}\n'
        return equip
    def elegir_sup(self):
        print(f'{self.nombre} deben elegir un superheroe para luchar:\n')
        print(self.get_equipo())
        x=int(input())
        return x
    def __str__(self):
        pass





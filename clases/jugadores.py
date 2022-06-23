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
        print(f'{self.nombre} debe elegir un superheroe para luchar:\n')
        print(self.get_equipo())
        x=int(input())
        return x
    def __str__(self):
        pass

class combate_superheroes:
    def __init__(self,jugador1,jugador2):
        self.jugador1=jugador1
        self.jugador2=jugador2
    def combate_individual(self,sup1,sup2,mov1):
        while sup1.get_energia()>0 and sup2.get_energia()>0:
            sup1.fight_ataque(sup2,mov1)
            t=sup2.elergir_mov()
            sup2.fight_ataque(sup1,sup2.movimientos[t])
            s=sup1.elergir_mov()
            combate_superheroes.combate_individual(sup1,sup2,sup1.movimientos[s])
        else:
            if sup1.get_energia()==0:
                print(f"{sup1.alias} gano la batalla\n")
                self.jugador2.equipo.remove(sup2)
            else:
                print(f"{sup2.alias} gano la batalla\n")
                self.jugador1.equipo.remove(sup1)



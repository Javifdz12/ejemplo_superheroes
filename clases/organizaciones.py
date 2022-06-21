class organizacion:
    def __init__(self,nombre,superheroes):
        if type(nombre)!= str:
            raise Exception("nombre de ser str")
        else:
            self.nombre=nombre
        if type(superheroes)!= list:
            raise Exception("superheroes de ser una lista")
        else:
            self.superheroes=superheroes
    def get_nombre(self):
        return self.nombre
    def get_superheroes(self):
        for i in range(len(self.superheroes)):
            print(f'{i} - {self.superheroes[i].__str__()}\n ')
    def set_superheroes(self,x):
        self.superheroes.append(x)
    def no_eliminado(self):
        return self.superheroes!=[]
    def surrender(self):
        self.superheroes=[]
    def __str__(self):
        return f'La organizacion {self.nombre}, tiene los siguientes superheroes:\n {self.get_superheroes()}'







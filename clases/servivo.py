class ser_vivo:
    def __init__(self,energia):
        self.energia=energia
    def is_vivo(self):
        return self.energia>0
    def is_muerto(self):
        self.energia<=0
    def get_energia(self):
        return self.energia
    def set_energia(self,x):
        self.energia=x

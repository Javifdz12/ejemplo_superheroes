from clases.movimientos import movimiento_general,tipo_movimiento,movimiento_especifico
from clases.escenarios import Escenario
def main():
    patada=movimiento_general("patada",tipo_movimiento.ataque,80)
    escenario=Escenario.denombre("torre_stark")
    print(escenario.__str__())
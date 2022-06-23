import random
from clases.movimientos import movimiento_general,tipo_movimiento,movimiento_especifico
from clases.escenarios import Escenario
from clases.superheroes import superheroe, tipo_superheroe
from clases.organizaciones import organizacion


def main():

    firstNames = {"A":"Captain", "B":"Turbo", "C":"Galactic", "D":"The", "E":"Aqua", "F":"Fire",
    "G":"Iron", "H":"Super", "I":"Green", "J":"Phantom", "K":"Dark", "L":"Ghost", "M":"Professor",
    "N":"Atomic", "O":"Rock", "P":"Omega", "Q":"Rocket", "R":"Shadow", "S":"Agent", "T":"Silver",
    "U":"Wild", "V":"Wolf", "W":"Ultra", "X":"Wonder", "Y":"Doctor", "Z":"Star"}

    lastNames = {"A":"X", "B":"Shield", "C":"Machine", "D":"Justice", "E":"Beast", "F":"Wing",
    "G":"Arrow", "H":"Skull","I":"Blade", "J":"Bolt", "K":"Cobra", "L":"Blaze",
    "M":"Soldier", "N":"Strike", "O":"Falcon", "P":"Fang", "Q":"King", "R":"Surfer",
    "S":"Bot", "T":"Guard", "U":"Thing", "V":"Claw", "W":"Brain", "X":"Master", "Y":"Power", "Z":"Storm"}

    organizaciones=["A - Force", "Avengers", "Mercs for Money", "League of Realms", "Strange Academy", "X-Men"]

    print()
    print("!!!COMENZEMOS¡¡¡")
    print()

    #ELEGIR ESCENARIO
    x=input("Elige un escenario: torre_stark, santo_santuario, colegio_xavier: ")
    x=x.lower()
    escenario=Escenario.de_nombre(x)
    print()
    #CREAR LISTA SUPERHEROES
    nombres=list(firstNames.values())
    apellidos=list(lastNames.values())
    tipos=["humano","no_humano"]
    list_sup=[]

    for i in range(len(nombres)):
        nombre=nombres[i]
        apellido=apellidos[i]
        alias=nombre+""+apellido
        s=tipos[random.randint(0,1)]
        tipo=tipo_superheroe.de_nombre(s)
        sup=superheroe(i+1,alias,alias,tipo,escenario)
        list_sup.append(sup)

    list_costes=[]
    for i in list_sup:
        list_costes.append(i.get_coste())


    #CREAR ORGANIZACIONES
    a=len(list_sup)
    b=len(organizaciones)
    c=a/b
    #a=26, b=6, c=4.33 por tanto van a sobrar superheroes(en este caso habrá 3 superheroes por organizacion y sobraran 8)
    org_sup=[]
    print()
    print("<<< FORMACION DE LAS ORGANIZACIONES >>>")
    print()
    for i in range(len(organizaciones)):
        nombre=organizaciones[i]
        org=organizacion(nombre,[])
        print(f'Elige superheroes para la organizacion: {nombre}')
        print()
        while len(org.superheroes)<3:
            for j in range(len(list_sup)):
                print(f'{j} - {list_sup[j].__str__()}')
            x=int(input())
            org.set_superheroes(list_sup[x])
            list_sup.remove(list_sup[x])
        else:
            org_sup.append(org)

    sup_independientes=organizacion("Catalan_academy",list_sup)
    org_sup.append(sup_independientes)
    lista_monedas=[escenario.get_monedas(),escenario.get_monedas()]
    jugador1=[]
    jugador2=[]
    jugadores=[jugador1,jugador2]

    print()
    print("<<< EMPIEZA LA ELECCION DE LOS SUPERHEROES >>>")
    print()

    for i in range(len(lista_monedas)):
        while lista_monedas[i]>min(list_costes) and len(jugadores[i])<escenario.num_superheroes:
            print()
            print("<<< ESTAS SON LAS ORGANIZACIONES, SUS SUPERHEROES Y SUS CARACTERISTICAS >>>")
            print()
            for j in org_sup:
                print(j.__str__())
            print()
            print(f'Todavia dispone de {lista_monedas[i]} monedas')
            print()
            for j in range(len(org_sup)):
                if org_sup[j].superheroes!=[]:
                    print(f'{j}-{org_sup[j].nombre}\n')
            org=int(input(f"Jugador{i+1} elija una organización: "))
            print()
            for j in range(len(org_sup[org].superheroes)):
                print(f'{j}- {org_sup[org].superheroes[j].__str__()}')
            sup=int(input("Elija un superheroe: "))
            jugadores[i].append(org_sup[org].superheroes[sup])
            lista_monedas[i]=(lista_monedas[i]-org_sup[org].superheroes[sup].get_coste())
            org_sup[org].superheroes.remove(org_sup[org].superheroes[sup])


    print("\n<<< ELECCION DE MOVIMIENTOS POR PARTE DE CADA JUGADOR >>>\n")

    movs=[]
    movimiento1=movimiento_general("patada",tipo_movimiento.ataque,random.randint(1,15))
    movimiento2=movimiento_general("puñetazo",tipo_movimiento.ataque,random.randint(1,10))
    movimiento3=movimiento_general("escudo",tipo_movimiento.defensa,random.randint(1,12))
    movimiento4=movimiento_general("escupitajo",tipo_movimiento.defensa,random.randint(1,5))
    movimiento5=movimiento_general("espadazo",tipo_movimiento.ataque,random.randint(1,20))
    movs.append(movimiento1)
    movs.append(movimiento2)
    movs.append(movimiento3)
    movs.append(movimiento4)
    movs.append(movimiento5)

    movs_sup=[]
    for jugador in jugadores:
        for sup in jugador:
            print(f"Elige los movimientos de {sup.alias}\n")
            while len(sup.movimientos)<escenario.get_movimientos():
                for i in range(len(movs)):
                    print(f'{i}- {movs[i].__str__()}')
                x=int(input())
                movs_sup.append(movs[x])
            else:
                sup.set_movimientos(movs_sup)




















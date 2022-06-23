import random
from clases.movimientos import movimiento_general,tipo_movimiento,movimiento_especifico
from clases.escenarios import Escenario
from clases.superheroes import superheroe, tipo_superheroe
from clases.organizaciones import organizacion
from clases.jugadores import jugador,combate_superheroes


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
    for i in range(len(jugadores)):
        for sup in jugadores[i]:
            print(f"Jugador{i+1}elige los movimientos de {sup.alias}\n")
            while len(movs_sup)<escenario.get_movimientos():
                for j in range(len(movs)):
                    print(f'{j}- {movs[j].__str__()}')
                x=int(input())
                movs_sup.append(movs[x])
            else:
                sup.set_movimientos(movs_sup)

    print("\n<<< AHORA SI... !!!EMPIEZA LO BUENO¡¡¡ >>>\n")

    nombre_jug1=input(f'Jugador1 elija un nombre para su equipo: ')
    nombre_jug2=input(f'\nJugador2 elija un nombre para su equipo: ')
    jugador1=jugador(nombre_jug1,jugadores[0])
    jugador2=jugador(nombre_jug2,jugadores[1])
    combate=combate_superheroes(jugador1,jugador2)


    print("\n<<< EMPIEZA EL COMBATE >>>\n")

    while jugador1.equipo!=[] and jugador2.equipo!=[]:
        a=jugador1.elegir_sup()
        b=jugador2.elegir_sup()
        s=jugador1[a].elegir_mov()
        combate.combate_individual(jugador1.equipo[a],jugador2.equipo[b],jugador1.equipo[a].movimientos[s])
    else:
        if jugador1.equipo==[]:
            print(f"\n{jugador2.nombre} gano la guerra!!!!")
            print("<<< !!!ENHORABUENA¡¡¡ >>>")
        else:
            print(f"\n{jugador1.nombre} gano la guerra!!!!")
            print("<<< !!!ENHORABUENA¡¡¡ >>>")























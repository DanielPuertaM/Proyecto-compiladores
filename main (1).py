from arma import Arma, Baston, Espada, Pistola, crearArma


def menu():
    lista_de_armas = []
    narmas = 0

    while(True):
        print("1 - agregar arma nueva"+
            "\n2 - mostrar armas"+
            "\n3 - usar arma"+
            "\n4 - eliminar arma"+
            "\n0 - salir del juego")
        respuesta = input("Escoja su opción: ")
        if(respuesta == "1"):
            tipo_arma = input("Ingresa el tipo de arma\n1 - espada\n2 - pistola\n3 - bastón\n")
            if(tipo_arma in ["1", "2", "3"]):
                print("Ingrese un extra")
                print("Un material si es espada")
                print("Un tipo de arma para pistola")
                print("Un tipo magia si es bastón")
                extra = input()
                turnos = int(input("ingrese una cantidad de turnos para usar: "))
                ataque = int(input("Ingrese el daño por ataque por cada vez que se use: "))
                lista_de_armas.append(crearArma(tipo_arma, extra, turnos, ataque))
            
            narmas+=1
            pass
        elif(respuesta == "2"):
            for arma in lista_de_armas:
                print(arma.__str__())
        elif(respuesta == "3"):
            indice = int(input("Seleccione el indice del arma que desea usar: "))-1
            if(indice < narmas):
                lista_de_armas[indice].usar()
        elif(respuesta == "4"):
            indice = int(input("Seleccione el indice del arma que desea eliminar: "))-1
            if(indice < narmas):
                lista_de_armas.pop(indice)
                print("arma eliminada con exito")
            else:
                print("no existe un arma en ese indice")
        elif(respuesta == "0"):
            exit(0)
        else:
            print("Opción invalida")
menu()
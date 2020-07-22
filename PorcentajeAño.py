from datetime import date
from colorama import Fore, Back, Style


def imprimirBarra(porcentaje, lleno="█", vacio="-"):
    lleno = porcentaje * lleno
    vacio = (100 - porcentaje) * vacio
    barra = lleno + vacio
    if porcentaje <= 33: print(Fore.GREEN)
    elif porcentaje > 33 and porcentaje <= 66: print(Fore.YELLOW)
    else: print(Fore.RED)
    print(f"Progreso: |{barra}| {porcentaje}% completo\n")

def main():
    while True:
        while True:
            print("     Elija la acción a realizar")
            print("1. Progreso del año actual")
            des = input("2. Progreso entre un dia a seleccionar de ese mismo año    ")
            if des == '1':
                hoy = date.today()
                fin = date(hoy.year, 12, 31)
                dif = (fin - hoy).days
                prop = int((100*(365-dif))/365)
                imprimirBarra(prop)
                print("Para terminar el año faltan:")
                print("- {} dias".format(dif))
                print("- {} meses".format(round((dif / 30.4167),2)))
                print("- {} horas".format(dif * 24))
                print("- {} minutos".format(dif * 24 * 60))
                print("- {} segundos".format(dif * 24 * 60 * 60) + Fore.RESET)
                break
            elif des == '2':
                dia1 = input("Ingrese el dia de con el formato DD-MM-AAAA: ")
                dia1 = str(dia1).split('-')
                dia1 = date(int(dia1[2]), int(dia1[1]), int(dia1[0]))
                fin = date(dia1.year, 12, 31)
                dif = (fin - dia1).days
                prop = int((100 * (365 - dif)) / 365)
                imprimirBarra(prop)
                print("Para terminar el año faltan:")
                print("- {} dias".format(dif))
                print("- {} meses".format(round((dif / 30.4167),2)))
                print("- {} horas".format(dif * 24))
                print("- {} minutos".format(dif * 24 * 60))
                print("- {} segundos".format(dif * 24 * 60 * 60) + Fore.RESET)
                break
            else:
                print(Fore.RED + "Ingreso incorrecto. Reingresar.\n" + Fore.RESET)

        cont = input("Desea realizar otra consulta? [S/n] ")
        if cont == 'n' or cont == 'N':
            break




main()
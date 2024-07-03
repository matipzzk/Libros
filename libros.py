from funciones_libros import *

while True:
    limpiar()
    print("MENU")
    print("1.- Agregar libro")
    print("2.- Mostrar libros")
    print("3.- Buscar libro")
    print("4.- Actualizar libro")
    print("5.- CSV")
    print("6.- Salir")
    opc = int(input("Ingrese una opcion: "))
    limpiar()
    if opc==1:
        opc_1()
    elif opc==2:
        opc_2()
    elif opc==3:
        opc_3()
    elif opc==4:
        opc_4()
    elif opc==5:
        opc_5()
    else:
        opc_6()
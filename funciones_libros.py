import os, time, csv


libros = []


def opc_1():
    print("AGREGAR LIBRO")
    titulo =validar_nombre()
    autor = input("ingrese autor: ")
    anios = validar_numero()
    genero = input("ingrese genero: ")
    libro={
        "titulo":titulo, 
        "autor":autor, 
        "año":anios, 
        "genero":genero}
    libros.append(libro)
    
    
def opc_2():
    print("Mostrar libros")
    if len(libros)==0:
        print("No hay libros")
    else:
        for i in libros:
            print(f"Titulo: {i['titulo']} Año {i['año']} Genero: {i['genero']} Autor: {i['autor']}")
            time.sleep(4)

def opc_3():
    print("Buscar libro")
    if len(libros)==0:
        print("No hay libros")
    else:
        bustitulo = input("Ingrese titulo del libro: ")
        for x in libros:
            if x["titulo"]== bustitulo:
                print(f"Titulo: {x['titulo']} Año {x['año']} Genéro: {x['genero']} Autor: {x['autor']}")
            else:
                print("No existe!")
                
def opc_4():
    if len(libros)==0:
        print("No hay libros")
    else:
        bustitulo = input("Ingrese titulo del libro: ")
        for x in libros:
            if x["titulo"]== bustitulo:
                print(f"Titulo: {x['titulo']} Año {x['año']} Genéro: {x['genero']} Autor: {x['autor']}")
                print("Ingrese nueva información del libro")
                x["titulo"] = input("Ingrese titulo: ")
                x["autor"] = input("Ingrese autor: ")
                x["año"] = int(input("Ingrese año de publicacion: "))
                x["genero"] = input("Ingrese genero: ")
                print("Libro actualizado")
            else:
                print("No existe!")

def opc_5():
    if len(libros)==0:
        print("No hay libros")
    else:
        with open  ("libros.csv","w",newline="")as archivo:
            diccionario = ["titulo","autor","año","genero"]
            writer = csv.DictWriter(archivo, fieldnames=diccionario)
            writer.writeheader()
            writer.writerows(libros)
            print("Libros guardados en el archivo CSV exitosamente.")
            
def opc_6():
    print("Adios")
    exit()
    
    
    
def validar_nombre():
    while True:
        titulo = input("Ingrese titulo: ")
        if len(titulo) > 3:
            return titulo
        else:
            print("El titulo debe tener al menos 3 caracteres")
            
def validar_numero():
    while True:
        try:
            nro = int(input("Ingrese año: "))
            if nro > 0:
                return nro
            else:
                print("El año debe ser mayor a 0")
        except:
            print("Ingrese número entero")

def limpiar():
    os.system("cls")        
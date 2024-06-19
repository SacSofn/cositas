import json # le indico a el codigo que se usaran archivos y funciones json 
import random # le indico a el codigo que se usara funciones para numeros aleatorios
import os # le indico a el codigo que se usara funciones para ver paths y comandos de consola de windows
 
Cliente_json = "Cliente.json"

# NO ESTAN LAS VARIABLES CREADAS COMO GLOBALES YA QUE NO SE OCUPARAN MAS ADELANTE 

def limpiar_pantalla():
    # Detectar el sistema operativo y ejecutar el comando apropiado
    if os.name == 'nt':  # Si el sistema operativo es Windows
        os.system('cls')
    else:  # Si el sistema operativo es Unix/Linux/MacOS
        os.system('clear')

def archivo_existe(ruta_archivo):
    return os.path.exists(ruta_archivo) # verificar si el archivo se encuentra descargado en nuestro pc, utilizando,
# el import os / y el comando "os.path.exist" como dice el nombre, si el camino hacia el archivo existe
 
def cargar_datos():
    if archivo_existe(Cliente_json): # llamamos la definicion archivo_existe(), y le preguntamos sobre Cliente_json  
        with open(Cliente_json,"r") as Clientela: # si encuentra el archivo me lo abre con "r"
            yeison = json.load(Clientela) # le indicamos que "yeison (una lista)" es el que abre nuestro archivo
        return yeison # se lo devolvemos
    else:
        print("No hay datos de personas") # si archivo_existe() no lo encuentra, envez de tirar error nos crea una lista vacia
        return [] # la lista vacia que se crea si no se encuentra el archivo Cliente_json

# para crear el archivo con los datos del cliente
def guardado(datos):
    with open(Cliente_json,"w") as Clientela: # me escribe los datos guardados mas adelante con el "w"
        json.dump(datos, Clientela, indent=2) # le "bota" los datos a mi archivo "Clientela", con una identacion de 2 para que se vea mas ordenado

def menu_principal(): # lo primero que muestra a el iniciar
    
    print(''' 
 ===========================
=========AUTO SEGURO=========
        Menu principal
          
1) Guardar info del vehiculo
          
2) Buscar vehiculo

3) imprimir certificado   
                   
4) Salir.
=============================                 
''')
    
def menu_guardar(): # es la opcion 2 de el menu principal y guarda los datos ingresados por el usuario
    yeison = cargar_datos() # llama a la definicion "cargar_datos()" y se la asigna a "yeison"
    limpiar_pantalla() # llama a la definicion "limpiar_pantalla() de parte de el (import os)" me limpia la pantalla 
# PREGUNTAR DUEÑO DEL AUTO
    dueño = input("Registre su nombre: ")
    while not dueño.isalpha():
        print("Ingrese un nombre valido: ")
        dueño = input("Registre su nombre: ")
    limpiar_pantalla()

# PREGUNTAR PATENTE
    patente = input("Escriba la patente de el vehiculo: ")
    if not buscar_patente(yeison, patente):
        while len(patente) not in range(3,15):
            print("Patente erronea")        
            patente = input("Escriba la patente de el vehiculo: ")
    else:
        print("Ya existe esa patente")
        input()
        return
    
# PREGUNTAR TIPO DE VEHICULO 
    tipo = input('Ingrese tipo de vehiculo ("auto","moto","camion"): ')
    while True:
        if tipo.isalpha() == True:    
            if tipo == "auto" or tipo == "moto" or tipo == "camion":
                break
            else:
                print("No entra en la categoria")
                tipo = input('Ingrese tipo de vehiculo ("auto","moto","camion): ')
        else:
            print("Solo letras")
            tipo = input('Ingrese tipo de vehiculo ("auto","moto","camion): ')
    limpiar_pantalla()

# PREGUNTAR LA MARCA DEL VEHICULO
    marca = input("Escriba la marca de su vehiculo: ")
    while not marca.isalpha():
        print("Solo letras")
        marca = input("Escriba la marca de su vehiculo: ")
    limpiar_pantalla()

# PREGUNTAR EL PRECIO DEL VEHICULO
    print("El precio del vehiculo no debe se inferior a $5.000.000")
    precio = input("Escriba el precio de su vehiculo: ")
    while True:
        if precio.isnumeric() == True:
            if int(precio) <= 5000000:
                print("El precio del vehiculo no debe se inferior a $5mill")
                precio = input("Escriba el precio de su vehiculo: ")  
            else:
                print("Precio de vehiculo Valido!")
                break
        else:
            print("""
=================================
EL precio fue escrito con letras
=================================
                    """)
            print("El precio del vehiculo no debe se inferior a $5mill")
            precio = input("Escriba el precio de su vehiculo: ")
    limpiar_pantalla()

# PREGUNTAR MULTAS
    tiene_multas = input("Su auto tiene multas (1. si / 2. no): ")
    while not tiene_multas.isnumeric():
        print("Solo numeros")
        tiene_multas = input("Su auto tiene multas (1. si / 2. no): ")
    tiene_multas = int(tiene_multas)

    if tiene_multas == 1:    
        monto = input("Ingrese monto de la multa: ")
        while not monto.isnumeric():
            print("Solo Numeros")
            monto = input("Ingrese monto de la multa: ")
        fecha = input("ingrese fecha de la multa (ej: 07 06 2024): ")  

    elif tiene_multas == 2:
        monto = 0
        fecha = 0
    limpiar_pantalla()

# PREGUNTAR fecha de registro del vehículo     
    fechita = input("Ingrese la fecha de registro del vehículo (ej: 07 06 2024): ")
    limpiar_pantalla()

#=================== guardar los datos ingresados ===================   
    dict_clientes = { # guardo los datos en un diccionario
        "Patente": patente,
        "Cliente": dueño,
        "Tipo": tipo,
        "Marca": marca,
        "Precio": precio,
        "Fecha_registro": fechita,
        "Multas": [monto,fecha]
    }                       
    
    yeison = cargar_datos() # cargo los datos antes de guardarlos para que no se cree una lista aparte y que solo se guarden en la lista original
    yeison.append({patente: dict_clientes})
    guardado(yeison) 
    print("**** Progreso guardado! ****")
#=====================================================================

def buscar_patente(json_data, patente):
    for item in json_data:
        if patente in item:
            return item[patente]
    return False

def menu_buscar():
    yeison = cargar_datos()

    if yeison:
        patente = input("Ingrese la patente de el vehiculo: ")
        while True:
            if patente == "":
                print("Ingrese una patente valida")
                break
            else:
                print ("Buscando...")
                registro = buscar_patente(yeison, patente)
                if registro ==False:
                    print ("NO ENCONTRADO!")
                    break
                else:
                    print ("Patente: " , registro["Patente"])
                    print ("Cliente: " , registro["Cliente"])
                    print ("Tipo: " , registro["Tipo"])
                    print ("Marca: " , registro["Marca"])
                    print ("Precio: " , registro["Precio"])
                    print ("Fecha_registro: " , registro["Fecha_registro"])
                    print ("Multas [Monto, Fecha]: " , registro["Multas"])
                    input()
                    break
    

def imprimir_certificados():
    yeison = cargar_datos() # cargo los datos para ver si existe el archivo 
    
    patente = input("Ingrese la patente de el vehiculo: ") # pregunto primero cual es la patente que ingresara a el menu
    while True:
        if patente == "":
            print("Ingrese una patente valida") # validacion de la patente
            break
        else:
            break

    certificados = buscar_patente(yeison, patente) # le asigno una variable a la definicion "buscar_patente()" y que esta se encuentra en "yeison"
    if certificados: # si existe la patente y/o esta en el archivo "yeison" --> abre el menu
        while True: 
            print(f'''
======================= imprimir ========================       
1. certificados de Emisión de contaminantes: ${random.randint(1500, 3500)}
2. anotaciones vigentes: ${random.randint(1500, 3500)}
3. multas {random.randint(1500, 3500)}
4. Volver al menu principal
=========================================================    
''')
            
            opc = input("OPCION: ")
            while not opc.isnumeric():
                print("ingrese numeros")
                opc = input("OPCION: ")
            opc = int(opc)

            if opc == 1:
                print ("Patente: " , certificados["Patente"])
                print ("Cliente: " , certificados["Cliente"])
            elif opc == 2:
                print ("Patente: " , certificados["Patente"])
                print ("Cliente: " , certificados["Cliente"])
            elif opc == 3:
                print ("Patente: " , certificados["Patente"])
                print ("Cliente: " , certificados["Cliente"])
            elif opc == 4:
                break

    else:
        return     
        

# mostrar el menu principal
while True:
    menu_principal()

    opc = input("OPCION: ")
    while not opc.isnumeric():
      print("ingrese numeros")
      opc = input("OPCION: ")
    opc = int(opc)

    if opc == 1:
        menu_guardar()
    elif opc == 2:
        menu_buscar()
    elif opc == 3: 
        imprimir_certificados()
    elif opc == 4:
        print("Saliendo...")
        print("Creado por Lucas Salazar ")
        break
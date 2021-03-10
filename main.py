#-----------------------------------------------LIBRERIAS/MODULOS--------------------------------------------
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
#----------------------------------------------------CLASES--------------------------------------------------

#----------------------------------------------VARIABLES GLOBALES--------------------------------------------
ruta=""
#-----------------------------------------------FILE CHOOSER-------------------------------------------------
def obtenerArchivo():
    global ruta
    #Tk().withdraw() 
    try:
        ruta = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    except:
        print(" > ERROR: No se seleccionó ningún archivo o el archivo no cumple con el formato")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

#-------------------------------------------------MENU-------------------------------------------------------
def cargarMenu():
    obtenerArchivo()

def cargarOrden():
    if ruta!="":
       print("hola")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def generarMenu():
    if ruta!="":
        print("hola")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def generarFactura():
    if ruta!="":
        print("hola")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def generarArbol():
    if ruta!="":
        print("hola")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def salir():
    print("\n  > Nombre: Daniel Reginaldo Dubón Rodríguez")
    print("  > Carné: 201901772")
    print("  > Carrera: Ingeniería en Ciencias y Sistemas\n")
    print("  > Saliendo...\n")

def menu():
    opcion=0
    while opcion!=6:
        print("\n----------------------------------MENÚ PRINCIPAL----------------------------------\n")
        print("  ______________________________________________________________________________")
        print("  |                                                                             |")
        print("  |   - Curso: Lenguajes Formales y de Programación       ~ Sección: B+         |")
        print("  |   - Nombre: Daniel Reginaldo Dubón Rodríguez          ~ Carné: 201901772    |")
        print("  |   - Carrera: Ingeniería en Ciencias y Sistemas                              |")
        print("  ______________________________________________________________________________")
        print("\n   1. Cargar menú")
        print("   2. Cargar orden")
        print("   3. Generar menú")
        print("   4. Generar factura")
        print("   5. Generar árbol")
        print("   6. Salir\n")
        opcion=int(input("- Ingrese una opción:\n  > "))
        switch={1:cargarMenu, 2:cargarOrden, 3:generarMenu, 4:generarFactura, 5:generarArbol, 6:salir}
        func=switch.get(opcion,"Opción inválida")
        try:
            func()
        except:
            print("\n > Opción inválida...")
            input(" - PRESIONE ENTER PARA CONTINUAR...")
menu()
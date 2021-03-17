#-----------------------------------------------LIBRERIAS/MODULOS--------------------------------------------
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from Procesar import Analizar
from Funciones.ReporteMenuEr import generarR
Tk().withdraw()
#----------------------------------------------------CLASES--------------------------------------------------

#----------------------------------------------VARIABLES GLOBALES--------------------------------------------
rutaMenu=""
rutaOrden=""
#-----------------------------------------------FILE CHOOSER-------------------------------------------------

#-------------------------------------------------MENU-------------------------------------------------------
def cargarMenu():
    global rutaMenu
    print("\n----------------------------------CARGAR ARCHIVO----------------------------------\n")
    try:
        rutaMenu = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        if rutaMenu=="":
            print(" > ERROR: No se seleccionó ningún archivo")
            input("\n- PRESIONE ENTER PARA CONTINUAR...")
        else:
            print(" > Archivo cargado")
            input("\n- PRESIONE ENTER PARA CONTINUAR...")
    except:
        print(" > ERROR: No se seleccionó ningún archivo o el archivo no cumple con el formato")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def cargarOrden():
    print("\n----------------------------------CARGAR ARCHIVO----------------------------------\n")
    global rutaOrden
    try:
        rutaOrden = askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
        if rutaOrden=="":
            print(" > ERROR: No se seleccionó ningún archivo")
            input("\n- PRESIONE ENTER PARA CONTINUAR...")
        else:
            print(" > Archivo cargado")
            input("\n- PRESIONE ENTER PARA CONTINUAR...")
    except:
        print(" > ERROR: No se seleccionó ningún archivo o el archivo no cumple con el formato")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")
   

def generarMenu():
    print("\n-----------------------------------GENERAR MENÚ-----------------------------------\n")
    if rutaMenu!="":
        try:
            a=Analizar(rutaMenu)
            tokens=a.getListaTokens()
            errores=a.getListaErrores()
            if errores==None:
                print("  - ¿Desea poner un límite en los precios?")
                print("     1. Sí")
                print("     2. No\n")
                opcion=int(input("  - Ingrese una opción:\n     > "))
            else:
                print("  > ERROR: El archivo contiene errores")
                generarR(errores,tokens)
                input(" - PRESIONE ENTER PARA CONTINUAR...")
        except:
            print("  > ERROR: Ocurrio un error de análisis")
            input(" - PRESIONE ENTER PARA CONTINUAR...")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def generarFactura():
    print("\n-----------------------------------GENERAR ORDEN----------------------------------\n")
    if rutaOrden!="":
        print("hola")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def generarArbol():
    if rutaMenu!="":
        print("hola")
    else:
        print("  > ERROR: No se ha cargado ningún archivo")
        input("\n- PRESIONE ENTER PARA CONTINUAR...")

def salir():
    print("  > Saliendo...\n")

def menu():
    opcion=0
    while opcion!=6:
        print("\n----------------------------------MENÚ PRINCIPAL----------------------------------\n")
        print("   _____________________________________________________________________________ ")
        print("  |                                                                             |")
        print("  |   - Curso: Lenguajes Formales y de Programación       ~ Sección: B+         |")
        print("  |   - Nombre: Daniel Reginaldo Dubón Rodríguez          ~ Carné: 201901772    |")
        print("  |   - Carrera: Ingeniería en Ciencias y Sistemas                              |")
        print("  |_____________________________________________________________________________|")
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
from Clases.Datos import datos, error
from Clases.Dt import Seccion, Opciones
import re

class AnalizarOrden:
    def __init__(self, ruta):
       self.ruta=ruta
       self.Linea=1
       self.texto=""
       self.ListaTokens=[]
       self.ListaErrores=[]
       self.leerArchivo()

    def leerArchivo(self):
        archivo=open(self.ruta,'r', encoding='utf8')
        for linea in archivo:
           self.texto+=linea
        archivo.close() 
        self.analizar()
    
    def analizar(self):
        estado=0
        posicion=0
        columna=1
        string=""
        noIdentificados="~!@#$%^&*()_+-|;\/¿¡?{[}]´."
        longitud=len(self.texto)
        while posicion<longitud:

            caracter=self.texto[posicion]
            if estado==0:
                if caracter=="'":
                    estado=1
                    posicion+=1
                    columna+=1

                elif caracter==" ":
                    posicion+=1
                    columna+=1

                elif caracter=="\n":
                    posicion+=1
                    self.Linea+=1
                    columna=1

                elif caracter.isdigit():
                    estado=10
                    posicion+=1
                    columna+=1

                else:
                    posicion+=1
            
            elif estado==1:
                if caracter=="'":
                    aux=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux)
                    nombre=string
                    posicion+=1
                    columna+=1
                    estado=2
                    string=""
                elif caracter==",":
                    aux=error("'", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=3
                    string=""
                    aux=error("'", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=3
                    string=""
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado==2:
                if caracter==",":
                    estado=3
                    columna+=1
                    posicion+=1
                elif caracter==" ":
                    posicion+=1
                    columna+=1
                elif caracter in noIdentificados:
                    aux2=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                elif caracter.isdigit():
                    aux2=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                elif caracter=="'":
                    estado=4
            
            elif estado==3:
                if caracter=="'":
                    estado=1
                    columna+=1
                    posicion+=1
                elif caracter==" ":
                    posicion+=1
                    columna+=1
                elif caracter in noIdentificados:
                    aux2=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                elif caracter.isdigit():
                    estado=4

            elif estado==4:
                posicion+=1

    def imprimirTokens(self):
        cont=1
        for tokens in self.ListaTokens:
            print(cont,tokens)
            cont+=1

    def imprimirErrores(self):
        for errores in self.ListaErrores:
            print(errores)


    def verificarNumero(self,txt):
        cont=0
        for buscar in txt:
            if "." in buscar:
                cont+=1

        if cont==1:
            cadena=txt.split(".")
            if " " in cadena[0]:
                return "Formato inválido, no se aceptan espacios"
            elif  cadena[0]=="" or cadena[0].isdigit()==False:
                return "Formato inválido, se esperaba digitos antes del punto"
            else:
                if cadena[1].isdigit() or cadena[1].isspace() or cadena[1]=="":
                    if cadena[1].isspace() or cadena[1]=="":
                        txt+="00"
                        return txt
                    else:
                        if " " in cadena[1]:
                            return "Formato inválido, no se aceptan espacios"
                        elif len(cadena[1])>2:
                            aux=float(txt)
                            redondeado = round(aux, 2)
                            return  str(redondeado)
                        elif len(cadena[1])==2:
                            return txt
                        elif len(cadena[1])==1:
                            txt+="0"
                            return txt
                else:
                    return "Formato inválido, se esperaba o no digitos después del punto"

        elif cont>1:
            return  "Formato inválido, contiene mas dos puntos"

        elif cont==0:
            if txt.isdigit():
                txt+=".00"
                return txt
            else:
                return "Formato inválido, no son digitos"
    def getListaTokens(self):
        return self.ListaTokens
    
    def getListaErrores(self):
        return self.ListaErrores

        #print(self.contLinea, self.reservada, self.cadena, self.opciones, self.error)

a=AnalizarOrden("Archivos_Prueba\Orden.txt")
a.imprimirTokens()
a.imprimirErrores()

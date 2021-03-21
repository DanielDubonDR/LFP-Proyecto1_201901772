from Clases.Datos import datos, error
from Clases.Dt import Seccion, Opciones
import re

class Analizar:
    def __init__(self, ruta):
       self.ruta=ruta
       self.texto=""
       self.Linea=1
       self.contadorSecciones=0
       self.nombreRestaurtante=""
       self.ListaTokens=[]
       self.ListaErrores=[]
       self.ListaSecciones=[]
       self.ListaOpciones=[]
       self.leerArchivo()

    def leerArchivo(self):
        archivo=open(self.ruta,'r', encoding='utf8')
        for linea in archivo:
           self.texto+=linea
        archivo.close() 
        self.texto+="\n"
        self.analizar()
        self.buscarReservada()
    
    def analizar(self):
        estado=0
        posicion=0
        columna=1
        string=""
        noIdentificados="~!@#$%^&*()\,_+-|/¿¡?{[}]´."
        longitud=len(self.texto)
        idseccion=None
        identificador=None
        nombre=None
        precio=None
        descripcion=None
        while posicion<longitud:
            
            caracter=self.texto[posicion]
            if estado==0:
                if caracter=="r":
                    estado=1
                    string+=caracter
                    posicion+=1
                    columna+=1

                elif caracter==" ":
                    posicion+=1
                    columna+=1

                elif caracter=="\n":
                    posicion+=1
                    self.Linea+=1
                    columna=1

                elif caracter=="'":
                    estado=5
                    posicion+=1
                    columna+=1
                    self.contadorSecciones+=1

                elif caracter=="[":
                    estado=8
                    posicion+=1
                    columna+=1

                else:
                    posicion+=1
            
            elif estado==1:
                if string=="restaurante":
                    estado=2
                    aux=datos("restaurante", self.Linea, columna, "Palabra Reservada")
                    self.ListaTokens.append(aux)
                    string=""
                
                elif re.search(r"[a-z]",caracter):
                        string+=caracter
                        posicion+=1
                        columna+=1
                else:
                    if caracter=="=":
                        estado=2
                        #print("Palabra reservada no válida",string)
                        aux=error(string,self.Linea,columna,"Palabra reservada no válida")
                        self.ListaErrores.append(aux)
                        string=""

                    elif caracter=="'":
                        estado=3
                        #print("Palabra Reservada no valida",string)
                        #print("Se esperaba =")
                        aux=error(string,self.Linea,columna,"Palabra reservada no válida")
                        aux2=error("=",self.Linea,columna,"Se esperaba")
                        self.ListaErrores.append(aux)
                        self.ListaErrores.append(aux2)
                        string=""
                    else:
                        #print("Caracter no válido",caracter)
                        aux=error(caracter,self.Linea,columna,"Carácter no valido")
                        self.ListaErrores.append(aux)
                        string+=caracter
                        posicion+=1
                        columna+=1
                    
            elif estado==2:
                
                if caracter=="=":
                    estado=3
                    posicion+=1
                    columna+=1
        
                elif caracter=="'":
                    estado=3

                elif caracter==" ":
                    posicion+=1
                    columna+=1

                elif caracter.isalnum():
                    aux=error("='",self.Linea,columna,"Se esperaba")
                    self.ListaErrores.append(aux)
                    estado=4
                else:
                    aux2=error(caracter,self.Linea,columna,"Carácter inválido, es esperaba ='")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                
            elif estado==3:
                if caracter=="'":
                    estado=4
                    posicion+=1
                    columna+=1
                
                elif caracter==" ":
                    posicion+=1
                    columna+=1
                elif caracter.isalnum():
                    aux=error("'",self.Linea,columna,"Se esperaba")
                    self.ListaErrores.append(aux)
                    estado=4
                else:
                    aux2=error(caracter,self.Linea,columna,"Carácter inválido, se esperaba '")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                

            elif estado==4:
                if caracter=="'":
                    posicion+=1
                    estado=0
                    aux=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux)
                    self.nombreRestaurtante=string
                    string=""
                    columna+=1
                elif caracter=="\n":
                    aux=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux)
                    aux2=error("'",self.Linea,columna,"Se esperaba")
                    self.ListaErrores.append(aux2)
                    string=""
                    posicion+=1
                    estado=0
                
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1
            #---------------------trabajar aqui
            elif estado==5:
                if caracter=="'":
                    aux=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux)
                    posicion+=1
                    columna+=1
                    estado=6
                    z=Seccion(self.contadorSecciones,string)
                    self.ListaSecciones.append(z)
                    idseccion=self.contadorSecciones
                elif caracter==":":
                    aux=error("'", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=6
                elif caracter=="\n":
                    aux=error("':", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=0
                    string=""
                    posicion+=1
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado==6:
                if caracter==":":
                    #aux=datos(string.replace("'",""), self.Linea, columna, "Nombre de sección")
                    #self.ListaTokens.append(aux)
                    string=""
                    estado=0
                    posicion+=1
                    columna+=1
                elif caracter==" ":
                    posicion+=1
                    columna+=1
                elif caracter=="\n":
                    aux=error(":", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    #aux2=datos(string, self.Linea, columna, "Cadena")
                    #self.ListaTokens.append(aux2)
                    estado=0
                    string=""
                else:
                    aux=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux)
                    posicion+=1
                    columna+=1
            #trabajar aca    
            elif estado==8:
                if caracter==";":
                    verificar = re.search("[a-z][a-z0-9_]*",string)
                    if string.lstrip().rstrip()==verificar.group():
                        aux=datos(string.lstrip().rstrip(), self.Linea, columna, "Identificador")
                        self.ListaTokens.append(aux)
                        identificador=string.lstrip().rstrip()
                        estado=9
                        string=""
                        posicion+=1
                        columna+=1
                    else:
                        #print("identificador no valido", string.lstrip())
                        aux=error(string, self.Linea, columna, "Identificador inválido")
                        self.ListaErrores.append(aux)
                        estado=9
                        string=""
                        posicion+=1
                        columna+=1
                elif caracter=="'":
                    aux=error(";", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    verificar = re.search("[a-z][a-z0-9_]*",string)
                    if string.lstrip().rstrip()==verificar.group():
                        aux=datos(string.lstrip().rstrip(), self.Linea, columna, "Identificador")
                        self.ListaTokens.append(aux)
                        estado=10
                        string=""
                    else:
                        #print("identificador no valido", string.lstrip())
                        aux=error(string, self.Linea, columna, "Identificador inválido")
                        self.ListaErrores.append(aux)
                        estado=10
                        string=""
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado==9:
                if caracter=="'":
                    estado=10
                    posicion+=1
                    columna+=1
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
                else:
                    estado=10
                    aux=error("'", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
            
            elif estado==10:
                if caracter=="'":
                    aux=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux)
                    nombre=string
                    posicion+=1
                    columna+=1
                    estado=11
                    string=""
                elif caracter==";":
                    aux=error("'", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=12
                    string=""
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado==11:
                if caracter==";":
                    estado=12
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
                    estado=12
                    aux=error(";", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
            #---------------trabajar desde aqui, es recibir numero
            elif estado==12:
                if caracter==";":
                    posicion+=1
                    estado=13
                    numero=self.verificarNumero(string.rstrip().lstrip())
                    if "Formato" in numero:
                        aux2=error(string.rstrip().lstrip(),self.Linea,columna,numero)
                        self.ListaErrores.append(aux2)
                    else:
                        aux=datos(string.rstrip().lstrip(), self.Linea, columna, "Número")
                        self.ListaTokens.append(aux)
                        precio=numero
                    string=""
                    columna+=1
                elif caracter=="'":
                    numero=self.verificarNumero(string.rstrip().lstrip())
                    if "Formato" in numero:
                        aux2=error(string.rstrip().lstrip(),self.Linea,columna,numero)
                        self.ListaErrores.append(aux2)
                    else:
                        aux=datos(string.rstrip().lstrip(), self.Linea, columna, "Número")
                        self.ListaTokens.append(aux)
                    aux2=error("'",self.Linea,columna,"Se esperaba")
                    self.ListaErrores.append(aux2)
                    string=""
                    posicion+=1
                    estado=13
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

                

            elif estado==13:
                if caracter=="'":
                    estado=14
                    posicion+=1
                    columna+=1
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
                else:
                    estado=14
                    aux=error("'", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
            
            elif estado==14:
                if caracter=="'":
                    aux=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux)
                    descripcion=string
                    posicion+=1
                    columna+=1
                    estado=15
                    string=""
                    z=Opciones(idseccion,identificador,nombre,precio,descripcion)
                    self.ListaOpciones.append(z)
                elif caracter=="]":
                    aux=error("'", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=16
                    string=""
                elif caracter in noIdentificados:
                    aux2=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                elif caracter=="\n":
                    aux=error("']", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=16
                    string=""
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1
                
            
            elif estado==15:
                if caracter=="]":
                    posicion+=1
                    columna+=1
                    estado=16
                elif caracter=="\n":
                    aux=error("]", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    estado=16
                elif caracter in noIdentificados:
                    aux2=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado==16:
                estado=0

    def buscarReservada(self):
        for buscar in self.ListaTokens:
            encontrado=False
            if buscar.lexema=="restaurante":
                encontrado=True
            
        if encontrado==False:
            aux=error("restaurante", "0", "0", "No existe la palabra reservada")
            self.ListaErrores.append(aux)

    def imprimirTokens(self):
        cont=1
        for tokens in self.ListaTokens:
            print(cont,tokens)
            cont+=1

    def imprimirErrores(self):
        for errores in self.ListaErrores:
            print(errores)

    def imprimirSecciones(self):
        for errores in self.ListaSecciones:
            print(errores)

    def imprimirOpciones(self):
        for errores in self.ListaOpciones:
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

    def getListaSecciones(self):
        return self.ListaSecciones

    def getListaOpciones(self):
        return self.ListaOpciones

    def getNombre(self):
        return self.nombreRestaurtante

        #print(self.contLinea, self.reservada, self.cadena, self.opciones, self.error)
'''
a=Analizar("Archivos_Prueba\entrada.txt")
a.imprimirSecciones()
a.imprimirOpciones()
print(a.nombreRestaurtante)
a.imprimirTokens()
a.imprimirErrores()
'''

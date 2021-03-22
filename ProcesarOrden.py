from Clases.Datos import datos, error
from Clases.DatosOrden import dtCabecera, dtOrden
import re

class AnalizarOrden:
    def __init__(self, ruta,opciones):
       self.ruta=ruta
       self.Linea=1
       self.texto=""
       self.g=0
       self.ListaTokens=[]
       self.ListaErrores=[]
       self.opciones=opciones
       self.header=None
       self.ListaOrden=[]
       self.leerArchivo()


    def leerArchivo(self):
        archivo=open(self.ruta,'r', encoding='utf8')
        for linea in archivo:
           self.texto+=linea
           if linea!="\n":
               self.g+=1
        archivo.close() 
        self.texto+="\n"
        self.analizar()
    
    def analizar(self):
        estado=0
        posicion=0
        columna=1
        string=""
        cant=0
        noIdentificados="~!@#$%^&*()_+-|;\/¿¡?{[}]´."
        noIdentificados2="~!@#$%^&*()+-|;\/¿¡?{[}]´."
        cliente=""
        nit=""
        direccion=""
        cont=0
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
                    estado=5
                    string+=caracter
                    posicion+=1
                    columna+=1

                elif caracter in noIdentificados2:
                    aux=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux)
                    posicion+=1
                    columna+=1

                else:
                    posicion+=1
            
            elif estado==1:
                if caracter=="'":
                    aux=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux)
                    if cont==0:
                        cliente=string
                    elif cont==1:
                        nit=string
                    elif cont==2:
                        direccion=string
                    cont+=1
                    posicion+=1
                    columna+=1
                    estado=2
                    string=""
                elif caracter==",":
                    aux=error("'", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=2
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
                elif caracter=="'":
                    estado=1
                    aux=error(",", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    posicion+=1
                    columna+=1
                else:
                    if caracter.isdigit():
                        aux2=error(caracter, self.Linea, columna, "Carácter inválido")
                        self.ListaErrores.append(aux2)
                        posicion+=1
                        columna+=1
                    elif caracter.isalpha():
                        aux2=error(caracter, self.Linea, columna, "Carácter inválido")
                        self.ListaErrores.append(aux2)
                        posicion+=1
                        columna+=1
            
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
                if caracter=="%":
                    '''
                    aux=datos(string+caracter, self.Linea, columna, "Propina")
                    self.ListaTokens.append(aux)
                    '''
                    numero=self.verificarPorcentaje(string.rstrip().lstrip())
                    if "Formato" in numero:
                        aux2=error(string.rstrip().lstrip(),self.Linea,columna,numero)
                        self.ListaErrores.append(aux2)
                        aux=datos(string.rstrip().lstrip()+str("%"), self.Linea, columna, "Porcentaje")
                        self.ListaTokens.append(aux)
                    else:
                        aux=datos(string.rstrip().lstrip()+str("%"), self.Linea, columna, "Porcentaje")
                        self.ListaTokens.append(aux)
                        v=dtCabecera(cliente,nit,direccion,numero)
                        self.header=v
                    posicion+=1
                    columna+=1
                    estado=0
                    string=""
                elif caracter=="\n":
                    aux=error("%", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    numero=self.verificarPorcentaje(string.rstrip().lstrip())
                    if "Formato" in numero:
                        aux2=error(string.rstrip().lstrip(),self.Linea,columna,numero)
                        self.ListaErrores.append(aux2)
                        aux=datos(string.rstrip().lstrip()+str("%"), self.Linea, columna, "Porcentaje")
                        self.ListaTokens.append(aux)
                    else:
                        aux=datos(string.rstrip().lstrip()+str("%"), self.Linea, columna, "Porcentaje")
                        self.ListaTokens.append(aux)
                    estado=0
                    string=""
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1
            
            elif estado==5:
                if caracter==",":
                    aux=datos(string.rstrip().lstrip(), self.Linea, columna, "Número")
                    self.ListaTokens.append(aux)
                    asd=string.rstrip().lstrip()
                    try:
                        cant=int(asd)
                    except:
                        aux=error(string.rstrip().lstrip(), self.Linea, columna, "No es un numero entero")
                        self.ListaErrores.append(aux)
                    posicion+=1
                    columna+=1
                    estado=6
                    string=""
                elif caracter.isalpha():
                    aux=error(",", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string.rstrip().lstrip(), self.Linea, columna, "Número")
                    self.ListaTokens.append(aux2)
                    estado=6
                    string=""
                elif caracter in noIdentificados:
                    aux2=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado==6:
                if caracter=="\n":
                    verificar = re.search("[a-z][a-z0-9_]*",string)
                    if string.lstrip().rstrip()==verificar.group():
                        z=self.buscar(string.lstrip().rstrip())
                        if z==False:
                            aux=error(string.lstrip().rstrip(), self.Linea, columna, "El identificador no esta registrado")
                            self.ListaErrores.append(aux)
                        else:
                            aux=datos(string.lstrip().rstrip(), self.Linea, columna, "Identificador")
                            self.ListaTokens.append(aux)
                            f=dtOrden(z.nombre,z.precio, cant)
                            self.ListaOrden.append(f)
                        estado=0
                        string=""
                    else:
                        #print("identificador no valido", string.lstrip())
                        aux=error(string, self.Linea, columna, "Identificador inválido")
                        self.ListaErrores.append(aux)
                        estado=0
                        string=""
                if caracter==" " and self.g==1:
                    verificar = re.search("[a-z][a-z0-9_]*",string)
                    if string.lstrip().rstrip()==verificar.group():
                        z=self.buscar(string.lstrip().rstrip())
                        if z==False:
                            aux=error(string.lstrip().rstrip(), self.Linea, columna, "El identificador no esta registrado")
                            self.ListaErrores.append(aux)
                        else:
                            aux=datos(string.lstrip().rstrip(), self.Linea, columna, "Identificador")
                            self.ListaTokens.append(aux)
                            f=dtOrden(z.nombre,z.precio, cant)
                            self.ListaOrden.append(f)
                        estado=0
                        string=""
                    else:
                        #print("identificador no valido", string.lstrip())
                        aux=error(string, self.Linea, columna, "Identificador inválido")
                        self.ListaErrores.append(aux)
                        estado=0
                        string=""
                elif caracter in noIdentificados2:
                    aux2=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux2)
                    posicion+=1
                    columna+=1
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1
                    
    def buscar(self, identifica):
        encontrado=False
        aux=None
        for i in self.opciones:
            if i.identificador==identifica:
                encontrado=True
                aux=i
        if encontrado:
            return aux
        else:
            return encontrado

    def imprimirTokens(self):
        cont=1
        for tokens in self.ListaTokens:
            print(cont,tokens)
            cont+=1

    def imprimirErrores(self):
        for errores in self.ListaErrores:
            print(errores)

    def imprimirOrden(self):
        for errores in self.ListaOrden:
            print(errores)

    def verificarPorcentaje(self,txt):
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
                if cadena[1].isdigit():
                    if len(cadena[1])>2:
                        aux=float(txt)
                        redondeado = round(aux, 2)
                        if aux<=100:
                            return  str(redondeado)
                        else:
                            return "Formato inválido, la propina debe ser menor al 100%"
                    elif len(cadena[1])==2:
                        aux=float(txt)
                        if aux<=100:
                            return txt
                        else:
                            return "Formato inválido, la propina debe ser menor al 100%"
                    elif len(cadena[1])==1:
                        aux=float(txt)
                        if aux<=100:
                            return txt
                        else:
                            return "Formato inválido, la propina debe ser menor al 100%"
                else:
                    return "Formato inválido, se esperaba digitos despues del punto"

        elif cont>1:
            return  "Formato inválido, contiene mas dos puntos"

        elif cont==0:
            if txt.isdigit():
                aux=float(txt)
                if aux<=100:
                    return txt
                else:
                    return "Formato inválido, la propina debe ser menor al 100%"
            else:
                return "Formato inválido, no son digitos"

    def getListaTokens(self):
        return self.ListaTokens
    
    def getListaErrores(self):
        return self.ListaErrores

    def getCabeceras(self):
        return self.header

    def getOrden(self):
        return self.ListaOrden

        #print(self.contLinea, self.reservada, self.cadena, self.opciones, self.error)
'''
a=AnalizarOrden("Archivos_Prueba\Orden.txt","as")
a.imprimirTokens()
a.imprimirErrores()
'''

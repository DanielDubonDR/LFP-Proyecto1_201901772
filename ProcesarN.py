from Clases.Datos import datos, error
import re

class Analizar:
    def __init__(self, ruta):
       self.ruta=ruta
       self.texto=""
       self.Linea=1
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
        longitud=len(self.texto)
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
                else:
                    string+=caracter
                    posicion+=1
                    columna+=1

            elif estado==6:
                if caracter==":":
                    aux=datos(string.replace("'",""), self.Linea, columna, "Nombre de sección")
                    self.ListaTokens.append(aux)
                    string=""
                    estado=0
                    posicion+=1
                    columna+=1
                elif caracter==" ":
                    posicion+=1
                    columna+=1
                elif caracter=="\n":
                    aux=error("':", self.Linea, columna, "Se esperaba")
                    self.ListaErrores.append(aux)
                    aux2=datos(string, self.Linea, columna, "Cadena")
                    self.ListaTokens.append(aux2)
                    estado=0
                else:
                    aux=error(caracter, self.Linea, columna, "Carácter inválido")
                    self.ListaErrores.append(aux)
                    posicion+=1
                    columna+=1
            #trabajar aca    
            elif estado==8:
                posicion+=1

    def imprimirTokens(self):
        for tokens in self.ListaTokens:
            print(tokens)

    def imprimirErrores(self):
        for errores in self.ListaErrores:
            print(errores)


        '''
        if linea.startswith("r"):
            columna=1
            estado=0
            string=""
            for caracter in linea:
                if estado==0:
                    if string.rstrip()=="restaurante":
                        estado=1
                        asd=str("[No = ")+str(self.contador)+str(",    Lexema = ")+str(string)+str(",   Fila = ")+str(self.contLinea)+str(",    Columna = ")+str(columna)+str(",   Token = Palabra Reservada]")
                        print(asd)
                        string=""
                        self.contador+=1

                    elif caracter=="=":
                        estado=2

                    elif caracter=="'":
                        estado=3

                    else:
                        if re.search(r"[a-z]",caracter):
                            string+=caracter
                        else:
                            string+=caracter
                            print("caracter desconocido",caracter)

                if estado==1:
                    if caracter=="=":
                        columna+=1
                        asd=str("[No = ")+str(self.contador)+str(",    Lexema = ")+str(caracter)+str(",    Fila = ")+str(self.contLinea)+str(",    Columna = ")+str(columna)+str(",    Token = Signo Igual]")
                        #print(asd)
                        #self.contador+=1
                        estado=2
                        continue
                    elif caracter=="'":
                        print("ERROR, se esperaba =")
                        estado=100
                        #-----------------------------corregir
                    elif re.search(r"[^']",caracter):
                        print("ERROR, se esperaba = y '")
                        estado=100
                
                if estado==2:
                    if caracter=="'":
                        columna+=1
                        asd=str("[No = ")+str(self.contador)+str(",    Lexema = ")+str(caracter)+str(",    Fila = ")+str(self.contLinea)+str(",    Columna = ")+str(columna)+str(",   Token = Apostrofe]")
                        #print(asd)
                        #self.contador+=1
                        estado=3
                        continue
                    elif caracter==" ":
                        columna+=1
                        continue
                    else:
                        print("Error: hace falta '")
                        estado=100
                if estado==3:
                    if caracter!="'":
                        string+=caracter
                    else:
                        asd=str("[No = ")+str(self.contador)+str(",    Lexema = ")+str(string)+str(",   Fila = ")+str(self.contLinea)+str(",    Columna = ")+str(columna)+str(",    Token = Cadena]")
                        print(asd)       
                        estado=100
                
                columna+=1
            

        elif linea.startswith("'"):
            columna=1
            estado=0
            string=""
            for caracter in linea:
                if estado==0:
                    if caracter=="'":
                        estado=1
                        columna+=1
                        continue
                        
                if estado==1:        
                    if caracter!="'":
                        string+=caracter
                    else:
                        self.contador+=1
                        asd=str("[No = ")+str(self.contador)+str(",    Lexema = ")+str(string)+str(",   Fila = ")+str(self.contLinea)+str(",    Columna = ")+str(columna)+str(",    Token = Cadena]")
                        print(asd)
                        estado=100
                columna+=1
                    

        if linea.startswith("["):
            columna=1
            estado=0
            string=""
            for caracter in linea:
                if estado==0:
                    if caracter=="[":
                        estado=1
                        columna+=1
                        continue
                if estado==1:
                    if caracter!=";":
                        if caracter==" ":
                            columna+=1
                            continue
                        else:
                            string+=caracter
                    else:
                        self.contador+=1
                        asd=str("[No = ")+str(self.contador)+str(",    Lexema = ")+str(string)+str(",   Fila = ")+str(self.contLinea)+str(",    Columna = ")+str(columna)+str(",    Token = Identificador]")
                        print(asd)
                        estado=2
                        string=""
                        continue
                if estado==2:
                    if caracter=="'":
                        estado=3
                        continue
                
                if estado==3:
                    if caracter!="'":
                        string+=caracter
                    else:
                        self.contador+=1
                        asd=str("[No = ")+str(self.contador)+str(",    Lexema = ")+str(string)+str(",   Fila = ")+str(self.contLinea)+str(",    Columna = ")+str(columna)+str(",    Token = Cadena]")
                        print(asd)
                        estado=4
                        string=""
                        continue

                if estado==4:
                    if caracter==";":
                        columna+=1
                        estado=5
                        continue

                    elif caracter==" ":
                        columna+=1
                
                if estado==5:
                    if caracter!=";":
                        if caracter==" ":
                            columna+=1
                            continue
                        else:
                            string+=caracter
                    else:
                        self.contador+=1
                        asd=str("[No = ")+str(self.contador)+str(",    Lexema = ")+str(string)+str(",   Fila = ")+str(self.contLinea)+str(",    Columna = ")+str(columna)+str(",    Token = Numero]")
                        print(asd)
                        estado=6
                        string=""
                        continue

                if estado==6:
                    if caracter=="'":
                        columna+=1
                        estado=7
                        continue
                    elif caracter==" ":
                        columna+=1

                if estado==7:
                    if caracter!="'":
                        string+=caracter
                    else:
                        self.contador+=1
                        asd=str("[No = ")+str(self.contador)+str(",    Lexema = ")+str(string)+str(",   Fila = ")+str(self.contLinea)+str(",    Columna = ")+str(columna)+str(",    Token = Cadena]")
                        print(asd)
                        estado=8
                        string=""
                        continue        
                columna+=1
                '''
        #print(self.contLinea, self.reservada, self.cadena, self.opciones, self.error)

a=Analizar("entrada.txt")
a.imprimirTokens()
a.imprimirErrores()

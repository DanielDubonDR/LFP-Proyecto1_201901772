import re

class Analizar:
    def __init__(self, ruta):
       self.ruta=ruta
       self.contador=1
       self.leerLinea()

    def leerLinea(self):
        self.contLinea=1
        self.reserv=""
        archivo=open(self.ruta,'r', encoding='utf8')
        for linea in archivo.readlines():
            if linea=="\n":
                self.contLinea+=1
                continue
            self.leerCaracteres(linea.lstrip().strip())
            self.contLinea+=1
        archivo.close() 
    
    def leerCaracteres(self, linea):

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
            '''
            if "=" in linea:
                for caracter in linea:
                    if estado==0:
                        if caracter!="=":
                            string+=caracter
                        else:
                            if string.rstrip()=="restaurante":
                                reservada=string
                                print("reservada",reservada,"Linea",self.contLinea,"Columna",cont)
                                estado=1
                            else:
                                print("no se reconoce",string, "Linea",self.contLinea,"Columna",cont)
                                estado=1
                            string=""

                    if estado==1:
                        if caracter!="'":
                            string+=caracter
                        else:
                            estado==3
                        print(string)
                    cont+=1

        else:
            self.reservada=False
        '''

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
        if self.reservada and self.cadena and self.opciones:
            self.error=False
        else:
            self.error=False
        '''
        #print(self.contLinea, self.reservada, self.cadena, self.opciones, self.error)
print("\nIngrese la ruta del archivo: ")
ruta=input(" > ")
print("\n")
a=Analizar(ruta)

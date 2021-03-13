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
            limpiar=False
            for caracter in linea:
                if estado==0:
                    if string.rstrip()=="restaurante":
                        estado=1
                        asd=str("No = ")+str(self.contador)+str(", Lexema = ")+str(string)+str(", Fila = ")+str(self.contLinea)+str(", Columna = ")+str(columna)+str(", Token = Palabra Reservada")
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
                        asd=str("No = ")+str(self.contador)+str(", Lexema = ")+str(caracter)+str(", Fila = ")+str(self.contLinea)+str(", Columna = ")+str(columna)+str(", Token = Signo Igual")
                        print(asd)
                        self.contador+=1
                        estado=2
                    elif caracter=="'":
                        print("ERROR, se esperaba =")
                        estado=100
                        #-----------------------------corregir
                    elif str.isalpha(caracter):
                        print("ERROR, se esperaba = y '")
                        estado=100
                
                if estado==3:
                    if caracter=="'":
                        columna+=1
                        asd=str("No = ")+str(self.contador)+str(", Lexema = ")+str(caracter)+str(", Fila = ")+str(self.contLinea)+str(", Columna = ")+str(columna)+str(", Token = Signo Igual")
                        print(asd)
                        self.contador+=1
                        estado=2
                    elif caracter=="'":
                        print("ERROR, se esperaba =")
                        estado=100
                    elif re.search(r"[^]",caracter):
                        print("ERROR, se esperaba = y '")
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

        '''
        if linea.startswith("'"):
            self.cadena=True
        else:
            self.cadena=False

        if linea.startswith("["):
            self.opciones=True
        else:
            self.opciones=False
            
        if self.reservada and self.cadena and self.opciones:
            self.error=False
        else:
            self.error=False
        '''
        #print(self.contLinea, self.reservada, self.cadena, self.opciones, self.error)

a=Analizar("entrada.txt")
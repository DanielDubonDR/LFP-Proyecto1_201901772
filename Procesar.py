
class Analizar:
    def __init__(self, ruta):
       self.ruta=ruta
       self.Preservada="restaurante"
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
            cont=1
            reservada=""
            estado=0
            string=""
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
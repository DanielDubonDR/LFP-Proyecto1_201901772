
class Analizar:
    def __init__(self, ruta):
       self.ruta=ruta
       self.Preservada="restaurante"
       self.espera=False
       self.reservada=False
       self.cadena=False
       self.opciones=False
       self.error=False
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
        self.contColumna=0

        if self.espera==False:
            if linea.startswith("r"):
                self.reservada=True
            else:
                self.reservada=False

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
        
        #print(self.contLinea, self.reservada, self.cadena, self.opciones, self.error)

a=Analizar("entrada.txt")
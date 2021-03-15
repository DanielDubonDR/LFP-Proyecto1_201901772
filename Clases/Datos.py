class datos:
    def __init__(self, lexema,linea, columna, token):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.token = token

    def __str__(self):
        string=str("Lexema: ")+str(self.lexema)+str(" Linea: ")+str(self.linea)+str(" Columna : ")+str(self.columna)+str(" Token: ")+str(self.token)
        return string

class error:
    def __init__(self, lexema, Linea, columna, descripcion):
        self.lexema = lexema
        self.Linea = Linea
        self.columna = columna
        self.descripcion=descripcion

    def __str__(self):
        string=str("Linea: ")+str(self.Linea)+str(" Columna : ")+str(self.columna)+str(" Carácter: ")+str(self.lexema)+str(" Descripcion: ")+str(self.descripcion)
        return string
class Seccion:
    def __init__(self, id, seccion):
        self.id=id
        self.seccion=seccion
    def __str__(self):
        string=str(self.id)+str(" ")+str(self.seccion)
        return string

class Opciones:
    
    def __init__(self):
        self.idseccion=None
        self.identificador=None
        self.nombre=None
        self.precio=None
        self.descripcion=None
       

    def setIdseccion(self, idseccion):
        self.idseccion=idseccion
    
    def setIdentificador(self, identificador):
        self.identificador=identificador

    def setNombre(self, nombre):
        self.nombre=nombre

    def setPrecio(self, precio):
        self.precio=precio

    def setDescripcion(self, descripcion):
        self.descripcion=descripcion

    def __str__(self):
        string=str(self.idseccion)+str(" ")+str(self.identificador)+str(" ")+str(self.nombre)+str(" ")+str(self.precio)+str(" ")+str(self.descripcion)
        return string    

'''
    def __init__(self, idseccion, identificador, nombre, precio, descripcion):
        self.idseccion=idseccion
        self.identificador=identificador
        self.nombre=nombre
        self.precio=precio
        self.descripcion=descripcion
    '''
'''
a=Opciones()
a.setIdseccion(1)
a.setIdentificador(2)
a.setNombre(3)
a.setPrecio(4)
a.setDescripcion(5)

print(a)
'''
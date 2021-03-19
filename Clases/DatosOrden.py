class dtOrden:
    def __init__(self, nombre, precio, cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
    
    def __str__(self):
        string=str(self.nombre)+str(" ")+str(self.precio)+str(" ")+str(self.cantidad)
        return string

class dtCabecera:
    def __init__(self, cliente, nit, direccion,propina):
        self.cliente=cliente
        self.nit=nit
        self.direccion=direccion
        self.propina=propina
    
    def __str__(self):
        string=str(self.cliente)+str(" ")+str(self.nit)+str(" ")+str(self.direccion)+str(" ")+str(self.propina)
        return string
        
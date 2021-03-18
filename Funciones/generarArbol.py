from graphviz import Digraph


def generarA(nombre,secciones,opciones):
    a=sorted(opciones)
    dot = Digraph(comment='Grafica')
    dot.node('0', nombre)
    for s in secciones:
        dot.node(str(s.id), str(s.seccion))
        dot.edge('0',str(s.id))
    
    for o in a:
        string=str(o.nombre)+str("   Q")+str(o.precio)+str("\n")+str(o.descripcion)
        dot.node(str(o.identificador), string)
        dot.edge(str(o.idseccion),str(o.identificador))

    #print(dot.source)
    dot.render('Arbol/arbolMenu.dot', view=True)
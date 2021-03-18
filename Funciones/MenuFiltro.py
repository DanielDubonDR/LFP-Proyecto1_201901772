import os
import random
texto=""
colores=["red","pink","purple","deep-purple","indigo","green","deep-orange","black"]
def cabecera(nombre):
    global texto
    texto=""
    c='''
    <!DOCTYPE html>
        <html>
            <title>Menu</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
            <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Asap+Condensed:wght@400;700&family=Courgette&family=Lobster&family=Rokkitt:wght@300;800&display=swap" rel="stylesheet">
            <style>
                .w3-lobster
                {
                    font-family: "Lobster", Sans-serif;
                }
                .w3-Asap-Condensed
                {
                    font-family: 'Asap Condensed', sans-serif;
                }
                .w3-Courgette
                {
                    font-family: 'Courgette', cursive;
                }
                .w3-Rokkitt
                {
                    font-family: 'Rokkitt', serif;
                    font-weight: 800;
                }
            </style>
            <body>
                <div class="w3-container w3-teal w3-center w3-margin-bottom">
                    <br>
                    <h1 class="w3-lobster" style="font-size: 60px;">'''+nombre+'''</h1>
                    <br>
                </div>
        '''
    texto+=c
def quitarDescripcion(string):
    if "Descripción" in string:
        return string.replace("Descripción","")
    elif "descripción" in string:
        return string.replace("descripción","")
    elif "descripcion" in string:
        return string.replace("descripcion","")
    elif "Descripcion" in string:
        return string.replace("Descripcion","")
    else:
        return string

def generarCuerpo(secciones, opciones,lim):
    global texto
    texto+="<br>"
    for sec in secciones:
        color=colores[random.randint(0,7)]
        texto+='''
            <div class="w3-container  w3-margin-bottom" >
                    <div class="w3-card-4 w3-margin-bottom">
                        <header class="w3-container w3-'''+str(color)+'''  w3-round-small">
                            <h1 class="w3-Rokkitt">'''+str(sec.seccion)+'''</h1>
                        </header>
                        <div class="w3-container w3-middle Asap-Condensed">
                            <table class="w3-table w3-margin-top">
                                <tr>
                                    <th style="width:33%;" class="w3-center w3-xlarge w3-Courgette">Nombre</th>
                                    <th style="width:33%;" class="w3-center w3-xlarge w3-Courgette">Descripción</th>
                                    <th style="width:33%;" class="w3-center w3-xlarge w3-Courgette">Precio</th>
                                </tr>
        '''
        for op in opciones:
            if sec.id==op.idseccion and float(op.precio)<=lim:
                texto+='''
                <tr>
                          <td class="w3-center w3-Asap-Condensed w3-large">'''+str(op.nombre)+'''</td>
                          <td class="w3-center w3-Asap-Condensed w3-large">'''+str(quitarDescripcion(op.descripcion))+'''</td>
                          <td class="w3-center w3-Asap-Condensed w3-large">Q'''+str(op.precio)+'''</td>
                        </tr>
                '''
        texto+='''
        </table>
                            <br>
                        </div>
                        <footer class="w3-container w3-'''+str(color)+''' w3-round-small"><br></footer>
                    </div>
                <br>
                </div>
        '''
    texto+='''
    <br>
    </body>
    </html>
    '''


def crearArchivo():
    global texto
    arhcivo=open('Menu.html','w')
    arhcivo.write(texto)
    arhcivo.close()
    os.startfile("Menu.html")

def generarFl(nombre, secciones, opciones,lim):
    cabecera(nombre)
    generarCuerpo(secciones, opciones, lim)
    crearArchivo()
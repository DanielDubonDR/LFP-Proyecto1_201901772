import os
import datetime as datetime
x = datetime.datetime.now()
fecha=str(x.strftime("%d"))+str("/")+str(x.strftime("%m"))+str("/")+str(x.strftime("%Y"))
texto=""

def cabecera(nombre, datos):
    global texto
    texto=""
    c='''
    <!DOCTYPE html>
    <html lang="es">
    <title>Factura</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Asap+Condensed:wght@400;700&family=Courgette&family=Lobster&family=Rokkitt:wght@300;800&display=swap"
        rel="stylesheet">
    <style>
        .w3-lobster {
            font-family: "Lobster", Sans-serif;
        }

        .Asap-Condensed {
            font-family: 'Asap Condensed', sans-serif;
        }

        .Courgette {
            font-family: 'Courgette', cursive;
        }

        .Rokkitt {
            font-family: 'Rokkitt', serif;
            font-weight: 800;
        }
    </style>

    <body>
        <div class="w3-display-container" style="height: 780px;" >
            <dir class="w3-display-middle" style="width: 550px;">
                <div class="w3-card-4 w3-margin-bottom">
                    <header class="w3-container w3-black  w3-round-small">
                        <p class="w3-lobster w3-center" style="font-size: 30px;">'''+str(nombre)+'''</p>
                    </header>
                    <div class="w3-container w3-middle Asap-Condensed">
                        <p class="w3-center" >Factura No. 01 <br> Fecha '''+str(fecha)+''' </p>
                        <p>Datos del Cliente: <br><br> <b>Nombre:</b> '''+str(datos.cliente)+''' <br> <b>Nit: </b>'''+str(datos.nit)+''' <br> <b>Dirección:</b> '''+str(datos.direccion)+''' <br><br> Descripción:</p>
                        <table class="w3-table w3-margin-top">
                            <tr>
                                <th style="width:25%;" class="w3-center  w3-Courgette">Cantidad</th>
                                <th style="width:25%;" class="w3-center  w3-Courgette">Concepto</th>
                                <th style="width:25%;" class="w3-center  w3-Courgette">Precio</th>
                                <th style="width:25%;" class="w3-center  w3-Courgette">Total</th>
                            </tr>
        '''
    texto+=c


def generarCuerpo(datos, elementos):
    global texto
    subTotal=0
    texto+="<br>"
    for items in elementos:
        total=float(items.cantidad)*float(items.precio)
        subTotal+=total
        texto+='''
            <tr>
                <td class="w3-center w3-Asap-Condensed ">'''+str(items.cantidad)+'''</td>
                <td class="w3-center w3-Asap-Condensed ">'''+str(items.nombre)+'''</td>
                <td class="w3-center w3-Asap-Condensed ">Q'''+str(items.precio)+'''</td>
                <td class="w3-center w3-Asap-Condensed ">Q'''+str("{0:.2f}".format(total))+'''</td>
            </tr>
        '''
    porcentaje=float(datos.propina)/100
    propina=(subTotal*porcentaje)  
    Tt=subTotal+propina
    texto+='''
        </table>
                        <p>----------------------------------------------------------------------------------------------------------------------------</p>
                        <table class="w3-table w3-margin-top">
                            <tr>
                                <td style="width:25%;" class=" w3-Courgette">Sub total</td>
                                <td style="width:25%;" class=" w3-Courgette"></td>
                                <td style="width:25%;" class=" w3-Courgette"></td>
                                <td style="width:25%;" class="w3-center w3-Courgette">Q'''+str("{0:.2f}".format(subTotal))+'''</td>
                            </tr>
                            <tr>
                                <td style="width:25%;" class=" w3-Courgette">Propina ('''+str(datos.propina)+'''%)</td>
                                <td style="width:25%;" class=" w3-Courgette"></td>
                                <td style="width:25%;" class=" w3-Courgette"></td>
                                <td style="width:25%;" class="w3-center w3-Courgette">Q'''+str("{0:.2f}".format(propina))+'''</td>
                            </tr>
                        </table>
                        <p>----------------------------------------------------------------------------------------------------------------------------</p>
                        <table class="w3-table w3-margin-top">
                            <tr>
                                <th style="width:25%;" class=" w3-Courgette">Total</th>
                                <th style="width:25%;" class=" w3-Courgette"></th>
                                <th style="width:25%;" class=" w3-Courgette"></th>
                                <th style="width:25%;" class="w3-center  w3-Courgette">Q'''+str("{0:.2f}".format(Tt))+'''</th>
                            </tr>
                        </table>
                    </div>
                    <footer class="w3-container w3-black  w3-round-small">
                        <br>
                    </footer>
                </div>
            </dir>
            <br>
        </div>
    </body>
    </html>
    '''


def crearArchivo():
    global texto
    arhcivo=open('Factura.html','w')
    arhcivo.write(texto)
    arhcivo.close()
    os.startfile("Factura.html")

def generarFac(nombre, datos, elementos):
    cabecera(nombre, datos)
    generarCuerpo(datos, elementos)
    crearArchivo()
from datetime import datetime
import os
texto=""
now = datetime.now()

def cabecera():
    global texto
    texto=""
    c="""<!DOCTYPE html>
    <html>
    <title>Reporte Errores</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lobster">
    <style>
    .w3-lobster {
        font-family: "Lobster", serif;
    }
    </style>

    <body>
    <div class="w3-container w3-teal w3-center w3-margin-bottom">
        <br><br>
        <h1 class="w3-lobster w3-xxxlarge">Reporte Orden</h1>
        <br><br>
    </div>
    
    <div class="w3-container w3-center">
        <div class="w3-container w3-lobster">
        <p class="w3-xxxlarge">Tabla de Errores<p>
        </div>
        <table class="w3-table-all w3-margin-top w3-card-4 w3-hoverable">
        <tr class="w3-pink">
            <th style="width:10%;" class="w3-center">No.</th>
            <th style="width:15%;" class="w3-center">Línea</th>
            <th style="width:15%;" class="w3-center">Columna</th>
            <th style="width:20%;" class="w3-center">Carácter</th>
            <th style="width:40%;" class="w3-center">Descripción</th>
        </tr>
        """
    texto+=c
def imprimirErr(errores):
    global texto
    cont=1
    for e in errores:
        texto+='''
        <tr>
        <td class="w3-center">'''+str(cont)+'''</td>
        <td class="w3-center">'''+str(e.Linea)+'''</td>
        <td class="w3-center">'''+str(e.columna)+'''</td>
        <td class="w3-center">'''+str(e.lexema)+'''</td>
        <td class="w3-center">'''+str(e.descripcion)+'''</td> 
        </tr>
        '''
        cont+=1

def imprimirTK(tokens):
    global texto
    texto+='''
    </table>
  </div><br><br>

  <div class="w3-container w3-center">
    <div class="w3-container w3-lobster">
      <p class="w3-xxxlarge">Tabla de Tokens<p>
    </div>
    <table class="w3-table-all w3-margin-top w3-card-4 w3-hoverable">
      <tr class="w3-black">
        <th style="width:10%;" class="w3-center">No.</th>
        <th style="width:30%;" class="w3-center">Lexema</th>
        <th style="width:15%;" class="w3-center">Fila</th>
        <th style="width:15%;" class="w3-center">Columna</th>
        <th style="width:30%;" class="w3-center">Token</th>
      </tr>
    '''
    cont=1
    for e in tokens:
        texto+='''
        <tr>
        <td class="w3-center">'''+str(cont)+'''</td>
        <td class="w3-center">'''+str(e.lexema)+'''</td>
        <td class="w3-center">'''+str(e.linea)+'''</td>
        <td class="w3-center">'''+str(e.columna)+'''</td>
        <td class="w3-center">'''+str(e.token)+'''</td> 
        </tr>
        '''
        cont+=1
    
    texto+='''
        </table>
    </div><br><br>
    <div class="w3-panel w3-light-grey w3-leftbar w3-rightbar w3-border-teal">
        <p><b>Reporte generado el:</b>&nbsp;'''+str(now)+'''</p>
    </div>
    <br>
    </body>

    </html>
    '''
def crearArchivo():
    global texto
    arhcivo=open('Reporte_Errores_Orden.html','w', encoding='utf8')
    arhcivo.write(texto)
    arhcivo.close()
    os.startfile("Reporte_Errores_Orden.html")

def generarRO(errores, tokens):
    cabecera()
    imprimirErr(errores)
    imprimirTK(tokens)
    crearArchivo()
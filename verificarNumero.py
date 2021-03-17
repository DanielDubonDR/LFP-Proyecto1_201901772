def verificarNumero(txt):
    cont=0
    for buscar in txt:
        if "." in buscar:
            cont+=1

    if cont==1:
        cadena=txt.split(".")
        if " " in cadena[0]:
            return "Formato inválido, no se aceptan espacios"
        elif  cadena[0]=="" or cadena[0].isdigit()==False:
            return "Formato inválido, se esperaba digitos antes del punto"
        else:
            if cadena[1].isdigit() or cadena[1].isspace() or cadena[1]=="":
                if cadena[1].isspace() or cadena[1]=="":
                    txt+="00"
                    return txt
                else:
                    if " " in cadena[1]:
                        return "Formato inválido, no se aceptan espacios"
                    elif len(cadena[1])>2:
                        aux=float(txt)
                        redondeado = round(aux, 2)
                        return  str(redondeado)
                    elif len(cadena[1])==2:
                        return txt
                    elif len(cadena[1])==1:
                        txt+="0"
                        return txt
            else:
                return "Formato inválido, se esperaba o no digitos después del punto"

    elif cont>1:
        return  "Formato inválido, contiene mas dos puntos"

    elif cont==0:
        if txt.isdigit():
            txt+=".00"
            return txt
        else:
            return "Formato inválido, no son digitos"

aux=verificarNumero("1.p")
print(aux)
if "Formato" in aux:
        
        print("si",aux)
else:
    print("nel",aux)
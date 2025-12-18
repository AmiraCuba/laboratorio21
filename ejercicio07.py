def copiar_texto(archivo1, archivo2):    
    with open(archivo1, "r") as f:
        contenido = f.read()
    with open(archivo2, "w") as f:
        f.write(contenido)

def copiar_binario(archivo1, archivo2):    
    with open(archivo1, "rb") as f:
        contenido = f.read()
    with open(archivo2, "wb") as f:
        f.write(contenido)
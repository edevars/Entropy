def leer():
    file = open("./books/libro1.txt","r")
    contenido = list()
    if file.mode == 'r':
        contenido = file.read()
    
    return contenido

if __name__== "__main__":
    contenido = leer()
    print(contenido)
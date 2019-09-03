def read_book(url):
    file = open(url,"r")
    contenido = list()
    if file.mode == 'r':
        contenido = file.read()
    
    return contenido

def fillZeros(size):
    finalSize = size -1
    lista = [0 for _ in range(finalSize)]

    return lista

def countRepetitions(book,abecedary):
    ABC_Cont = dict()
    size = len(abecedary)
    bookSize = len(book)

    for i in range(size):
        rep = 0
        current_symbol = abecedary[i]
        for j in range(bookSize):
            symbol = book[j] 
            if symbol == current_symbol:
                rep+=1
        ABC_Cont[current_symbol] = rep
    
    return ABC_Cont

if __name__== "__main__":
    book = read_book("./books/libro1.txt")
    bookSize = len(book) 

    ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    list_count = countRepetitions(book, ABC)
    print(list_count)
    
    
from math import log2

def read_book(url):
    file = open(url,"r")
    contenido = list()
    if file.mode == 'r':
        contenido = file.read()
    
    return contenido

def fillZeros(size):
    lista = [0 for _ in range(size)]

    return lista

def countRepetitions(book,alphabet):
    
    size = len(alphabet)
    bookSize = len(book)
    ABC_Cont = fillZeros(size)

    for i in range(size):
        rep = 0
        current_symbol = alphabet[i]
        for j in range(bookSize):
            symbol = book[j] 
            if symbol == current_symbol:
                rep+=1
        ABC_Cont[i] = rep
    
    return ABC_Cont

def entropyWithoutMemory(book, alphabet):
    list_count = countRepetitions(book, alphabet)
    sizeAlphabet = len(alphabet)
    Probability = fillZeros(sizeAlphabet)
    Information = fillZeros(sizeAlphabet)

    for i in range(sizeAlphabet):
        p_temp = list_count[i]/sum(list_count)
        Probability[i] = p_temp
        if p_temp != 0:
            Information[i] = log2(1/p_temp)
        else:
            Information[i] = 0

    h = fillZeros(len(Probability))
    for x in range(len(Probability)):
        h[x]=Probability[x]*Information[x]
    
    H = sum(h)

    return [Probability,Information,H]

if __name__== "__main__":
    book = read_book("./books/libro1.txt")
    bookSize = len(book) 

    ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    
    Probability, Information, H = entropyWithoutMemory(book, ABC)
    
    
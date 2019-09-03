from math import log2
import matplotlib.pyplot as plt
import numpy as np

def read_book(url):
    file = open(url,"r")
    contenido = list()
    if file.mode == 'r':
        contenido = file.read()
    
    return contenido

def fillZeros(size):
    lista = [0 for _ in range(size)]

    return lista

def countRepetitions(book,alphabeat):
    
    size = len(alphabeat)
    bookSize = len(book)
    ABC_Cont = fillZeros(size)

    for i in range(size):
        rep = 0
        current_symbol = alphabeat[i]
        for j in range(bookSize):
            symbol = book[j] 
            if symbol == current_symbol:
                rep+=1
        ABC_Cont[i] = rep
    
    return ABC_Cont

def entropyWithoutMemory(book, alphabeat):
    list_count = countRepetitions(book, alphabeat)
    sizeAlphabet = len(alphabeat)
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

def plot_bar_Probabilities(alphabeat,probabilities):
    # this is for plotting purpose
    index = np.arange(len(alphabeat))
    plt.figure(1)
    plt.bar(index, probabilities)
    plt.xlabel('Symbol', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.xticks(index, alphabeat, fontsize=10)
    plt.title('Probabilidades')

def plot_bar_Information(alphabeat,Information):
    # this is for plotting purpose
    plt.figure(2)
    index = np.arange(len(alphabeat))
    plt.bar(index, Information)
    plt.xlabel('Symbol', fontsize=12)
    plt.ylabel('Information', fontsize=12)
    plt.xticks(index, alphabeat, fontsize=10)
    plt.title('Información por simbolo')

if __name__== "__main__":
    book = read_book("./books/libro1.txt")
    bookSize = len(book) 

    ABC=['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','z',' ']
    
    Probability, Information, H = entropyWithoutMemory(book, ABC)
    plot_bar_Probabilities(ABC, Probability)
    plot_bar_Information(ABC, Information)
    plt.show()
    
    
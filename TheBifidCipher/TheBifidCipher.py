#Autor: Guadarrama Ortega Cesar Alejandro

# importamos la librería numpy, y le damos como nombre np dentro del programa
import numpy as np
# Importing itertools
import itertools
#import OrderedDict 
from collections import OrderedDict 


#Matirz con llave
lista_de_listas=[ ["_",0,1,2,3,4], 
                  [0,'E','N','C','R','Y'], 
                  [1,'P','T','A','B','D'],
                  [2,'F','G','H','I','K'],
                  [3,'L','M','O','Q','S'],
                  [4,'U','V','W','X','Z']
                  ]
matriz = np.array(lista_de_listas)


#Funcion para hacer sublistas   
def sublista(lista, conjunto):
    sub=[] ; resultado=[]
    for i in lista:
        sub+=[i]
        if len(sub)==conjunto: resultado+=[sub] ; sub=[]
    if sub: resultado+=[sub]
    return resultado
#Funcion para hacer una lista plana
def listaPlana(datos):
    listaPlana = []
    for item in datos:
        listaPlana+= item
    return listaPlana
    
def separarTexto(texto):
    lista = []
    for i in texto:
        lista.append(i)
    print("MENSAJE RECIBIDO")
    print(lista)
    return lista

def encontrarFilaColumna(lista):
    listaFilaColumna=[]
    for i in lista:
        filaColumna=np.where(matriz==i) #busca el valor en la matriz y assigna fila y columna
        numeroFilaColumna=list(itertools.chain(*filaColumna)) #convierte el array a una lista (fila y columna) 
        #Revisa si la coordenadas existen y le resta un espacio
        if bool(numeroFilaColumna):
            #nlist = [n-1 for n in numeroFilaColumna] otra forma restar a un elemento de una lista
            numeroFilaColumna[0]=numeroFilaColumna[0]-1
            numeroFilaColumna[1]=numeroFilaColumna[1]-1
            listaFilaColumna.append(numeroFilaColumna)
    return listaFilaColumna

def dividir_lista(lista):
    half = len(lista)//2
    return lista[:half], lista[half:]

def juntar_listas(lista1,lista2):
    combinacion=[]
    combinacionLista=[]
    combinacion = list(zip(lista1, lista2))
    combinacionLista = [list(element) for element in combinacion]
    return combinacionLista
#Funcion de encriptar
def encrypt(mensaje):
    #Variables
    textoCifrado = ""
    listaFilaColumna=[]
    lista = []
    #Extrae los caracteres y los almacena en una lista
    lista=separarTexto(mensaje)
    #Encuentra la fila y columna de cada caracter
    listaFilaColumna = encontrarFilaColumna(lista)
    #print(listaFilaColumna)
    #Acomodar valores de la lista
    listaOrdenada = [item[0] for item in listaFilaColumna]
    listaOrdenada2 = [item[1] for item in listaFilaColumna]
    mensajeCodificado = listaOrdenada+listaOrdenada2
    #print(mensajeCodificado)
    #Dividimos los pares de numero en una nueva lista
    coordenadasFinales=sublista(mensajeCodificado,2)
    #print(coordenadasFinales)
    #Encriptacion final del mensaje
    coordenadasFinalesPlano=listaPlana(coordenadasFinales)
    print("MENSAJE CODIFICADO")
    print(coordenadasFinalesPlano)
    listaMatriz = [n+1 for n in coordenadasFinalesPlano]
    #print(listaMatriz)
    coordenadasFinales=sublista(listaMatriz,2)
    for fila, columna in coordenadasFinales: 
        textoCifrado+=matriz[fila,columna]
    print("Texto cifrado: "+textoCifrado)

def decrypt(mensaje):
    #Variables
    lista = []
    listaPlanaCoordenadas = []
    listaFilaColumna=[]
    listaNuevasCoordenadas =[]
    listaNuevasCoordenadasPlana=[]
    textoDecifrado = ""
    #Extrae los caracteres y los almacena en una lista
    lista=separarTexto(mensaje)
    #Asigna las coordenadas
    listaFilaColumna = encontrarFilaColumna(lista)
    #print(listaFilaColumna)
    #Hacemos la lista plana
    listaPlanaCoordenadas=listaPlana(listaFilaColumna)
    #Dividimos en 2
    coordenadas1,coordenadas2=dividir_lista(listaPlanaCoordenadas)
    #print(coordenadas1)
    #print(coordenadas2)
    #Creamos la nueva lsista de listas con las coordenadas
    listaNuevasCoordenadas = juntar_listas(coordenadas1,coordenadas2)
    #print(listaNuevasCoordenadas)
    #La hacemos lista plana
    listaNuevasCoordenadasPlana=listaPlana(listaNuevasCoordenadas)
    print("MENSAJE DECODIFICADO")
    print(listaNuevasCoordenadasPlana)
    #Modificamos las coordenadas siguiendo la matriz principal
    listaMatriz = [n+1 for n in listaNuevasCoordenadasPlana]
    #Dcifrado final del mensaje
    coordenadasFinales=sublista(listaMatriz,2)
    for fila, columna in coordenadasFinales: 
        textoDecifrado+=matriz[fila,columna]
    print("Texto desifrado: "+textoDecifrado)
    
def main():
    print("          ****The Bifid cipher****")
    print("-----------------------------------------")
    print("@autor: Guadarrama Ortega Cesar Alejandro")
    print("-----------------------------------------")
    print("Matriz con llave:ENCRYPT ")
    print(matriz)
    while True:
        print("          ****The Bifid cipher****")
        print("-----------------------------------------")
        instruccion=input("¿Que quieres hacer Cifrar, Decifrar o Salir?: ")
        if instruccion == "Cifrar":
            encrypt(input("Introduce el mensaje a cifrar: "))
        elif instruccion =="Decifrar":
            decrypt(input("Introduce el mensaje a decifrar: "))
        elif instruccion =="Salir":
            break
        else:
            print("Escribe la opcion correcta")
    #encrypt(input("Introduce el mensaje a cifrar: "))
    #decrypt(input("Introduce el mensaje a decifrar: "))
if __name__ =="__main__":
    main()

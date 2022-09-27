"""@autor:BitPlanet"""

#Funcion que castea la llave de string a una lista de caracteres
def keyList(key):
    lista = []
    for i in key:
        lista.append(i)
    print("KEY RECIBIDA")
    print(lista)
    return lista
    
#Funcion que convierte el caracter de una lista a codigo ASCII 
def wordToASSCII(lista):
    listAux=[]
    for i in lista:
        listAux.append(ord(i))
    return listAux
    
#Funcion que convierte el codigo ASCII de una lista  a caracter
def ASCIItoWord(lista):
    listAux=[]
    for i in lista:
        listAux.append(chr(i))
    return listAux
    
#Funcion para Algoritmo de programación de claves (Key-scheduling algorithm ) 
def KSA(key): 
    S=[]
    for i in range(256):
        S.append(i)
    j=0
    for i in range(256):
        j = (j + S[i] + key[i%len(key)])%256
        aux=S[i]
        S[i]=S[j]
        S[j]=aux
    return (S)
    
#Funcion del algoritmo de generación pseudoaleatoria (PRGA)
def PRGA(S,message):
    i=j=k=0
    keyStream=[]
    while k < len(message):
        i = (i + 1)%256
        j = (j + S[i])%256
        #Swap S[i] y S[j]
        aux=S[i]
        S[i]=S[j]
        S[j]=aux
        keyStream.append(S[(S[i] + S[j])%256])
        k+= 1
    return keyStream
   
"""Funcion que convierte una lista 
de enteros a una lista de valores hexadeximales"""
def integerToHexadecimal(lista):
    listAux=[]
    for i in lista:
        listAux.append(hex(i)[2:])
    return listAux
    
"""Funcion que realiza operacion logica XOR
    de dos listas"""  
def XOR(list1,list2):
    res_list = [] 
    for i in range(0, len(list1)): 
        res_list.append(list1[i] ^ list2[i])
    return (res_list)

"""Funcion que convierte una lista de strings
 a una lista de enteros"""     
def stringToIntegerList(lista):
    listaAux = []
    listaAux = [int(x) for x in lista]
    return listaAux
    
#Funcion para cifrar     
def cipher():
    clave = keyList(input("Introduce la key: "))
    key=wordToASSCII(clave)
    SVector=KSA(key)
    message=wordToASSCII(input("Escribe el mensaje a cifrar en texto: "))
    keyStream=PRGA(SVector,message)
    print("\nLa KeyStream es: ")
    print(keyStream)
    cifrado= XOR(keyStream,message)
    print("---------------------------------------")
    print("\nEl texto cifrado es: ")
    print(cifrado)
    cifradoHex =integerToHexadecimal(cifrado)
    print("---------------------------------------")
    print("\nEl texto cifrado en Hexadecimal es: ")
    print(cifradoHex)

#Funcion para descifrar   
def descipher():
    clave = keyList(input("Introduce la key: "))
    key=wordToASSCII(clave)
    SVector=KSA(key)
    message =input("Escribe el mensaje a descifrar (valores enteros) poniendo espacios: ")
    messageSplit=message.split()
    messageF=stringToIntegerList(messageSplit)
    keyStream=PRGA(SVector,messageF)
    print("\nLa KeyStream es: ")
    print(keyStream)
    descifrado= XOR(keyStream,messageF)
    print("---------------------------------------")
    print("\nEl texto descifrado es: ")
    print(descifrado)
    descifradoHex =integerToHexadecimal(descifrado)
    print("---------------------------------------")
    print("\nEl texto descifrado en Hexadecimal es: ")
    print(descifrado)
    descifradoText=ASCIItoWord(descifrado)
    descifradoF = "".join(descifradoText)
    print("---------------------------------------")
    print("El texto descifrado en texto es: "+descifradoF)


#Funcion principal 
def main():
    print("@autor: BitPlanet")
    print("-----------------------------------------")
    while True:
        print("          ****Rivest Cipher 4 (RC4)****")
        print("-----------------------------------------")
        instruccion=input("¿Que quieres hacer Cifrar, Descifrar o Salir?: ")
        if instruccion == "Cifrar":
            cipher()
            print("\n")
        elif instruccion =="Descifrar":
            descipher()
            print("\n")
        elif instruccion =="Salir":
            break
        else:
            print("Escribe la opcion correcta")
if __name__ =="__main__":
    main()


#Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

lista = [1,2,3,4,5,8,9,7,6]

def agregar():
    numero= int(input("Digite un numero: "))
    lista.append(numero)
    print(lista)

agregar()

def orden():
    lista2 =[1,2,3,4,5,6,7,8,9,10]
    lista3 =[13,11, 14,15,16,17,18,12, 19,20]
    lista2.sort()
    lista3.sort()
    print(lista2)
    print(lista3)
orden()
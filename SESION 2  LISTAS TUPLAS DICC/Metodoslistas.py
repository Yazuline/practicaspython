#listas mutables se pueden modificar, []  en otros lenguajes son llamadas arreglos y en python pueden tener distintos datos
#Metodos 
# append() Agregar datos a una lista  
# del lista[0] si conozco el indice elimina cosas de una lista  
# extend  se unen las listas que yo especifique, es como concatenar lista.extend(lista2)  
# remove sin conocer el indice puedo eliminar el elemento que se especifique  
# sotr() Me permite ordenar la lista  lista.sort()
 

lista= ["tomate", "cebolla", "Huevos", "arroz"]
lista2 =[1,2,3,4,5]
lista3= [6,7,8,9,10]
lista4=['a','c','d','b',]
print(lista)
print(lista2)
print(lista3)
print (lista2 + lista3)
print (lista[2], lista2[4])
lista[0] ="Camarones"
lista.append("Lentejas")
print(lista)
lista4.sort()
print(lista4)
del lista3[4]
print(lista3)


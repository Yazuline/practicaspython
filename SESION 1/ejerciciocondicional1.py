# Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal
letra = input("Ingrese una letra: ")

if letra in "aeiou":
    print("Es una Vocal")
elif letra in "0123456789":
        print("Es un número")
else:
    print("Es una Letra")
#elif letra in "0123456789":
    #print("Es un número")

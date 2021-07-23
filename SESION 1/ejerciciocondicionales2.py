rima1=input("Escriba una palabra: ")
rima2 =input("Escriba otra palabra: ")

if  rima1[-3::] == rima2[-3::]:
    print("Las 2 palabras riman")
elif rima1[-2::]==rima2[-2::]:
    print("Medio riman")
else:
    print ("Las 2 palabras no riman")
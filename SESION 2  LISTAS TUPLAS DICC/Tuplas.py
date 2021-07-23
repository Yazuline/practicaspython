meses = ('Enero', 'Febrero','Marzo','Abril', 'Mayo','Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre','Noviembre', 'Diciembre')
print(meses)
num= int(input("Digite un numero del 1 al 12: "))

if (num >=0 and num <=12):
        print("Ha seleccionado el mes: ", meses[num-1])
else:
    print("Valor digitado no corresponde")

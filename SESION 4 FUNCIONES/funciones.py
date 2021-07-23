def tablas(numero):
     i=0
     multi=0
    
     while i <=10:
        multi = numero * i
        print("{} * {} = {}".format(numero,i, multi))
        i+= 1
tablas(10)
def rango(a,b):
    primos=[]
    for n in range (a,b+1):
        contador=0
        for i in range(1,n+1):
            if n%i==0:
                contador+=1
        if contador==2:
            primos.append(n)
    return(primos)
print(rango(1,100000))



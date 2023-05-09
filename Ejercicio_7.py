a=int(input('ingresa el primer numero: '))
b=int(input('ingresa el segundo numero: '))
if a==b :
    print(a , ' es igual a ', b)
    if b>=a :
        print(b , ' es mayor igual a ', a)      

elif a!=b :
    print(a , ' es diferente a ', b)
    if a>b :
        print(a , ' es mayor que ', b)
    elif b>=a :
        print(b , ' es mayor igual a ', a)

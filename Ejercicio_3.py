a=int(input('ingresa el primer numero: '))

b=int(input('ingresa el segundo numero: '))
t='puedes realizar las siguientes operaciones \n- SUMA ingrese 1 \n- RESTA ingrese 2 \n- MULTIPLICACION ingrese 3 \n- DIVISION ingrese 4 \n- DIVISION ENTERA ingrese 5'
print(t)
c=str(input('ingresa la operacion que desee realizar: '))
if c.upper()=='1' :
    print(int(a+b))
elif c.upper()=='2' :
    print(int(a-b))
elif c.upper()=='3' :
    print(int(a*b))
elif c.upper()=='4' :
    print(int(a/b))
elif c.upper()=='5' :
    print(int(a//b))
else:
    print('Opcion ingresada es invalida')
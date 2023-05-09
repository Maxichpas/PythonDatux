def Area():
    print("""Se calculara el area las siguientes figuras:
- Un Circulo
- Un Cuadrado 
- Un Triangulo
Usando tan solo el radio""")
    pi=float(3.1415)
    r=float(input('Ingrese el valor del radio en cm: '))
    C = ((r)**2)*pi
    Cu=(2*(r**2))
    T=(r**2)
    print('Area del Circulo es ' , C)
    print('Area del Cuadrado es ' , Cu)
    print('Area del Triangulo es ' , T)

Area()
def paso1(a,b):
    if a%b == 0:
        r=a+b
        print(r)

def paso2(a,b):
    if b > 0 and a>b:
        r=a/b
        print(r)
        
def paso3(a,b):
    if a<b :
        r=b-a
        print(r)


def main(a,b):
    paso1(a,b)
    paso2(a,b)
    paso3(a,b)

main(1,3)
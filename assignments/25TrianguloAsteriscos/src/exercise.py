
def main():
    #Escribe tu código debajo de esta línea
    a = int(input("altura?"))
    d = a

    for x in range(a):
        d = d - 1
        w = "*" * (x+1)
        print(" " * d + w)
        
        
        

    pass


if __name__=='__main__':
    main()

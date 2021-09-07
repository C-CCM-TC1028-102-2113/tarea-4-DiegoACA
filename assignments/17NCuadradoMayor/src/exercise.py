

def main():
    #Escribe tu código debajo de esta línea

    n = int(input("#"))
    x = 1
    w = x

    while w < n:
        x = x + 1
        w = x**2
        
    print(x)
        
    pass

if __name__=='__main__':
    main()

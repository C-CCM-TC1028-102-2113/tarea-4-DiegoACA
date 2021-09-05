def main():
    #escribe tu código abajo de esta línea
    n = int(input("#"))

    if n >= 0:
        for x in range(1, n+1):
            if x % 2 == 1:
                print(str(x) + "-#")
            elif x % 2 == 0:
                print(str(x) + "-%")
    else:
        print("datos invalidos")

if __name__=='__main__':   
    main()

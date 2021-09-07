def main():

    n = float(input("#"))
    flag = 0
    m = 0

    if n >= 0:
        while n >= 0:
            m = m + n
            n = float(input("#"))
            flag = flag + 1
        
        a = m / flag
        print(a)
    else:
        print("inout invalido")

    pass


if __name__=='__main__':
    main()

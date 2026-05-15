while True:
    x = input("Informe um valor: ")

    try:
        t = int(x)
        z = 10 / t
    except ValueError:
        print("Controlei o ValueError")
    except ZeroDivisionError:
        print("Controlei o 0 division")
    else:
        break

print("Terminei o programa")
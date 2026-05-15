x = input("Informe um valor: ")

try:
    t = int(x)
    z = 10 / t
except ValueError:
    print("Controlei o ValueError")
except ZeroDivisionError:
    print("Controlei o 0 division")
else:
    print("Sem dar erro!")
finally:
    print("Passei aqui - SEMPRE")

print("Terminei o programa")
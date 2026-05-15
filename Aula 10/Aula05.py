with open("Teste.ttt", "r") as arq:
    print(arq.name)
    print(arq.mode)
    print(arq.tell())
    print(arq.read())
    print("*"*20)
    print(arq.tell())
    arq.seek(0)
    print(arq.read())
with open("aula8.anselmo", "w") as arqW:
    with open("aula7.anselmo", "r") as arqR:
        while True:
            linha = arqR.readline()
            if linha == "":
                break

            if linha != "#33: Maria Wayne (Nota1: 7) (Nota2: 6)\n":
                arqW.write(linha)
            

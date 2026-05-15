import csv

with open("MeuCSV.csv", "w") as arq:
    w = csv.writer(arq)
    w.writerow(("Nome", "Nota1", "Nota2"))
    w.writerow(("Ezequiel Muriel", 10, 3))
    w.writerow(("Maria Chiquinha", 4, 4))
    w.writerow(("Paulo Kiko", 2, 6))
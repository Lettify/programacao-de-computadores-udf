import csv

with open("MeuCSV.csv", "r") as arq:
    r = csv.reader(arq)
    for lst in r:
        for ele in lst:
            print("Elemento: ", ele)
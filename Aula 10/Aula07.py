# Gera um arquivo com
# 50 nomes e sobrenomes aleatórios
# 50 notas1 aleatórios
# 50 notas2 aleatórios

import random

nomes = ["João", "Gustavo", "Maria", "Pedro", "Fernanda", "Rafael", "Lorraine", "Henrique", "Lukas", "Birtu", "Bernardo", "Adriano", "Ricardo", "Ronaldo", "Zebrinha"]
sobrenomes = ["Pereira", "Silva", "Sousa", "Rocher", "Pinheiro", "Gutenberg", "Wayne"]

nomes_completos = []

for i in range(1, 51):
    random_nome = random.choice(nomes) + " " + random.choice(sobrenomes)
    random_nota1 = random.randint(1, 10)
    random_nota2 = random.randint(1, 10)
    nomes_completos.append({ "id": i, "nome": random_nome, "nota1": random_nota1, "nota2": random_nota2 })

with open("aula7.anselmo", "w") as arq:
    texto = ""
    for i in nomes_completos:
        texto += "#" + str(i["id"]) + ": " + i["nome"] + " (Nota1: " + str(i["nota1"]) + ") (Nota2: " + str(i["nota2"]) + ")\n"
    arq.write(texto)
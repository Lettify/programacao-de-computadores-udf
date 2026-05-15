import json

with open("MeuJSON.json", "r") as arq:
    texto = arq.read()
    dic = json.loads(texto)

print(dic["linguagem"])
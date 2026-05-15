import json

dic = {
    "nome": "Guido Van Rossum",
    "linguagem": "Python",
    "similar": ["C", "Modular-3", "Lisp"]
}

with open("MeuJSON.json", "w") as arq:
    arq.write(json.dumps(dic))
from urllib.request import urlopen

resp = urlopen("https://testeanpad.org.br").read().decode('utf8')

with open("teste.html", "w") as arq:
    arq.write(resp)
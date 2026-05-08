lst = [1, 3, 2, 3, 2, 4, 6, 3]

# Criar função para obter valor e retornar V ou F
isPar = lambda n: n%2==0

print(lst)
print(list(filter(isPar, lst)))
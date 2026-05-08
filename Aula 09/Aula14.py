from functools import reduce

lst = [4, 2, 5, 6, 2, 1, 6]

# Somar todos os números da lista sem usar sum()
# Função vai ter que obter 2 valores e retornar 1 valor
# Reduce -> 2 elementos e reduz a função a 1

f = lambda x,y: x + y

print(reduce(f,  lst))
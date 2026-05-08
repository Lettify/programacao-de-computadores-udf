# Métodos tem o poder de se chamar a si mesmo, ou seja, de se auto invocar. Isso é chamado de recursão.

def fatorial(n):
    if n < 2:
        return 1
    return n * fatorial(n - 1)

print(fatorial(-44))
print(fatorial(5))
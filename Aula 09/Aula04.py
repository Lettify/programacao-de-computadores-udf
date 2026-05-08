def fatorial(n):
    if n < 2:
        return 1
    ft = n
    for i in range(2, n):
        ft *= i
    return ft

print(fatorial(-44))
print(fatorial(5))
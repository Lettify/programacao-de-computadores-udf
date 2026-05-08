# Calcular o Fatorial
# < 2 é igual a 1
# 5! = 5 * 4 * 3 * 2 * 1

x = 5

if x < 2:
    print(1)
else:
    ft = x
    for i in range(2, x):
        ft *= i
    print(ft)

# def fatorial(n):
#     if type(n) != int:
#         return False
    
#     if n < 2:
#         return 1
    
#     fator = 0
#     last_fator = 0

#     for i in range(n, 2, -1):
#         fator 
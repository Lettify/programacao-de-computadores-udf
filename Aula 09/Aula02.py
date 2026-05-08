def calcular(n1, n2):
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2

    return soma, subtracao, multiplicacao, divisao

soma, subtracao, multiplicacao, divisao = calcular(10, 3)
print(soma, subtracao, multiplicacao, divisao)
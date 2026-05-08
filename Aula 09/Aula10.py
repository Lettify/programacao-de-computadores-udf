def isPar(n):
    return n % 2 == 0 and "É par" or "É ímpar"

isPar2 = lambda n: n% 2 == 0 and "É par" or "É ímpar"
    
print(isPar(2))
print(isPar(3))
print(isPar2(2))
print(isPar2(3))
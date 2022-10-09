# Exercício 5: Escreva um algoritmo recursivo que
# identifica se um número é primo.


def temdivisor(n, i, j):
    if i > j:
        return False
    elif n % i == 0:
        return True
    else:
        return temdivisor(n, i + 1, j)


def is_prime_number(n):
    return n > 1 and not (temdivisor(n, 2, n - 1))


print(is_prime_number(997))

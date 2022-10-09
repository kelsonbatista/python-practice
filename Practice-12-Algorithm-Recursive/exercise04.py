# Exercício 4: Escreva um algoritmo recursivo para encontrar
# o máximo divisor comum (mdc) de dois inteiros.


def find_mdc(a, b):
    if b == 0:
        return a
    return find_mdc(b, a % b)


print(find_mdc(20, 10))

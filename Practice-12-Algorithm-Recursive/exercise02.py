# Exercício 1: Crie um algoritmo não recursivo para contar quantos
# números pares existem em uma sequência numérica (1 a n).

# Exercício 2: Transforme o algoritmo criado acima em recursivo.


def count_even_numbers(n):
    count = 0
    if n == 0:
        return count
    else:
        if n % 2 == 0:
            count += 1
        return count + count_even_numbers(n - 1)


print(count_even_numbers(20))

# Exercício 6: Escreva um algoritmo que recebe
# uma lista e retorne-a na ordem reversa.


def reverse(numbers):
    if len(numbers) <= 1:
        return numbers
    return [numbers[-1]] + reverse(numbers[:-1])


print(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

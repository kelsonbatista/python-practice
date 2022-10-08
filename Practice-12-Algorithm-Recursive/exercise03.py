# Exercício 3: Crie um algoritmo recursivo que encontre,
# em uma lista, o maior número inteiro.


def find_max_number(numbers):
    n = 0
    if len(numbers) <= 1:
        return numbers[0]
    else:
        if numbers[n] > numbers[n + 1]:
            numbers.pop(n + 1)
            return find_max_number(numbers)
        else:
            numbers.pop(n)
            return find_max_number(numbers)


print(find_max_number([100, 20, 310, 44, 523, 60, 70, 208, 199, 410]))

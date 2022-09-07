# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.

def average(list):
    numbers = 0
    for number in list:
        numbers += number
    return numbers / len(list)


print(average([3, 4, 5, 6]))

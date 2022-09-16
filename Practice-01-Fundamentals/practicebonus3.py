# Exercício 3: Crie uma função que receba um número inteiro N
# e retorne o somatório de todos os números de 1 até N.
# Por exemplo, para N = 5, o valor esperado será 15.


def sum(n):
    new_number = 0
    for number in range(n):
        new_number += number + 1
    print(new_number)


sum(5)

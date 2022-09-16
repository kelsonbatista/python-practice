# Exercício 2: Faça um programa que, dado um valor n qualquer,
# tal que n > 1, imprima na tela um triângulo retângulo com n
# asteriscos de base. Por exemplo, para n = 5 o triângulo terá
# 5 asteriscos na base:


def triangle(n):
    count = 0
    for row in range(n):
        count += 1
        print(count * "*")


triangle(5)

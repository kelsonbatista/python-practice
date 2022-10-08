# 🚀 Exercício 3 Utilize o módulo random da linguagem Python para
# gerar um array com 100 números. Cada um desses números deve ser a
# média de n números gerados aleatoriamente. Qual é a ordem de
# complexidade de tempo e de espaço deste programa?


import random


def generate_random_average(n):
    count = 0
    array = []
    while (count < 100):
        sum = 0
        for i in range(n):
            sum += random.randint(0, 100)
        count += 1
        array.append(sum // n)
    return (array, len(array))


print(generate_random_average(5))


def randomAverages(n):
    list_of_averages = []

    for _ in range(100):
        average = 0
        for _ in range(n):
            average += random.randrange(1, n)
        average = average//n
        list_of_averages.append(average)

    return list_of_averages


print(randomAverages(5))

# Exercício 3 Execute os algoritmos de ordenação por seleção
# e inserção, para as entradas de dados ordenadas, inversamente
# ordenadas e aleatórias. Em seguida, compare-os. Faça testes
# para entradas de tamanho 10.000, 100.000, 1.000.000.


from random import shuffle
import time


def selection(numbers, sample):
    start = time.time()
    n = len(numbers)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[i]:
                min_index = j
                current = numbers[i]
                numbers[i] = numbers[min_index]
                numbers[min_index] = current
    return f'Tempo [Selection {sample}]: {round(time.time() - start, 8)} s'
    # return numbers


def insertion(numbers, sample):
    start = time.time()
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        position = i - 1
        while position >= 0 and numbers[position] > key:
            numbers[position + 1] = numbers[position]
            position -= 1
        numbers[position + 1] = key
    return f'Tempo [Insertion {sample}]: {round(time.time() - start, 8)} s'
    # return numbers


def sort_ordered(size):
    ordenados = list(range(size))
    return ordenados


def sort_inverted(size):
    inversamente_ordenados = list(reversed(range(size)))
    return inversamente_ordenados


def sort_random(size):
    ordenados = list(range(size))
    aleatorios = ordenados[:]  # copia dos ordenados
    shuffle(aleatorios)  # embaralha eles
    return aleatorios


# print('============================ ORDENADOS ============================')
# print(ordenados)
# print('============================ INVERTIDOS ============================')
# print(inversamente_ordenados)
# print('============================ ALEATÓRIOS ============================')
# print(aleatorios)
print('=========================== SELECTION ==========================')
print(selection(sort_ordered(10000), '10K'))
print(selection(sort_inverted(10000), '10K'))
print(selection(sort_random(10000), '10K'))
print('-----------------------------------')
print(selection(sort_ordered(20000), '20K'))
print(selection(sort_inverted(20000), '20K'))
print(selection(sort_random(20000), '20K'))
print('-----------------------------------')
print(selection(sort_ordered(30000), '30K'))
print(selection(sort_inverted(30000), '30K'))
print(selection(sort_random(30000), '30K'))
print('-----------------------------------')
print(selection(sort_ordered(100000), '100K'))
print(selection(sort_inverted(100000), '100K'))
print(selection(sort_random(100000), '100K'))
print('=========================== INSERTION ==========================')
print(insertion(sort_ordered(10000), '10K'))
print(insertion(sort_inverted(10000), '10K'))
print(insertion(sort_random(10000), '10K'))
print('-----------------------------------')
print(insertion(sort_ordered(20000), '20K'))
print(insertion(sort_inverted(20000), '20K'))
print(insertion(sort_random(20000), '20K'))
print('-----------------------------------')
print(insertion(sort_ordered(30000), '30K'))
print(insertion(sort_inverted(30000), '30K'))
print(insertion(sort_random(30000), '30K'))
print('-----------------------------------')
print(insertion(sort_ordered(100000), '100K'))
print(insertion(sort_inverted(100000), '100K'))
print(insertion(sort_random(100000), '100K'))

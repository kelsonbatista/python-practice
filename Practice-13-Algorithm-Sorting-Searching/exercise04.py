# Exercício 3 Execute os algoritmos de ordenação por seleção
# e inserção, para as entradas de dados ordenadas, inversamente
# ordenadas e aleatórias. Em seguida, compare-os. Faça testes
# para entradas de tamanho 10.000, 100.000, 1.000.000.


from random import shuffle
import time


def merge(numbers, sample):
    # st = time.time()
    start = 0
    end = len(numbers)
    mid = end // 2
    left = numbers[start:mid]
    right = numbers[mid:end]
    left_index, right_index = 0, 0
    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
    return numbers
    # return f'Tempo [Selection {sample}]: {round(time.time() - st, 8)} s'


def bubble(numbers, sample):
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
print('=========================== MERGE ==========================')
# print(merge(sort_ordered(100), '10K'))
# print(merge(sort_inverted(100), '10K'))
print(merge(sort_random(100), '10K'))
# print('-----------------------------------')
# print(merge(sort_ordered(20000), '20K'))
# print(merge(sort_inverted(20000), '20K'))
# print(merge(sort_random(20000), '20K'))
# print('-----------------------------------')
# print(merge(sort_ordered(30000), '30K'))
# print(merge(sort_inverted(30000), '30K'))
# print(merge(sort_random(30000), '30K'))
# print('-----------------------------------')
# print(merge(sort_ordered(100000), '100K'))
# print(merge(sort_inverted(100000), '100K'))
# print(merge(sort_random(100000), '100K'))
# print('=========================== INSERTION ==========================')
# print(bubble(sort_ordered(10000), '10K'))
# print(bubble(sort_inverted(10000), '10K'))
# print(bubble(sort_random(10000), '10K'))
# print('-----------------------------------')
# print(bubble(sort_ordered(20000), '20K'))
# print(bubble(sort_inverted(20000), '20K'))
# print(bubble(sort_random(20000), '20K'))
# print('-----------------------------------')
# print(bubble(sort_ordered(30000), '30K'))
# print(bubble(sort_inverted(30000), '30K'))
# print(bubble(sort_random(30000), '30K'))
# print('-----------------------------------')
# print(bubble(sort_ordered(100000), '100K'))
# print(bubble(sort_inverted(100000), '100K'))
# print(bubble(sort_random(100000), '100K'))

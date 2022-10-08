import time


def multiply1(array1, test):
    start = time.time() * 1000
    entry = len(array1)
    result = []
    iterations = 0

    for number1 in array1:
        result.append(number1 * number1)
        iterations += 1

    end = time.time() * 1000
    print(f'Teste [x1] {test} - Entrada {entry} - {iterations} iterações \
    - Tempo de execução: {round(end - start, 8)} ms \
    - 1 iteração - {round((end - start) / iterations, 8)} ms')
    return result


def multiply2(array1, array2, test):
    start = time.time() * 1000
    entry = len(array1)
    result = []
    iterations = 0

    for number1 in array1:
        for number2 in array2:
            result.append(number1 * number2)
            iterations += 1

    end = time.time() * 1000
    print(f'Teste [x2] {test} - Entrada {entry} - {iterations} iterações \
    - Tempo de execução: {round(end - start, 8)} ms \
    - 1 iteração - {round((end - start) / iterations, 8)} ms')
    return result


def multiply3(array1, array2, array3, test):
    start = time.time() * 1000
    entry = len(array1)
    result = []
    iterations = 0

    for number1 in array1:
        for number2 in array2:
            for number3 in array3:
                result.append(number1 * number2 * number3)
                iterations += 1

    end = time.time() * 1000
    print(f'Teste [x3] {test} - Entrada {entry} - {iterations} iterações \
    - Tempo de execução: {round(end - start, 8)} ms \
    - 1 iteração - {round((end - start) / iterations, 8)} ms')
    return result


array1 = [1, 2, 3, 4, 5]
print('=============================== [O(n)] ===============================')
multiply1(array1, 1)
multiply1(array1 * 2, 2)
multiply1(array1 * 3, 3)
print('============================== [O(n^2)] ==============================')
multiply2(array1, array1, 1)
multiply2(array1 * 2, array1 * 2, 2)
multiply2(array1 * 3, array1 * 3, 3)
print('============================== [O(n^3)] ==============================')
multiply3(array1, array1, array1, 1)
multiply3(array1 * 2, array1 * 2, array1 * 2, 2)
multiply3(array1 * 3, array1 * 3, array1 * 3, 3)

import time


def multiply_arrays(array1, array2, test):
    start = time.time() * 1000
    entry = len(array1)
    result = []
    number_of_iterations = 0

    for number1 in array1:
        for number2 in array2:
            # print(f'Array 1 - {number1}:{number2} - Array 2')
            result.append(number1 * number2)
            number_of_iterations += 1

    end = time.time() * 1000
    print(f'Teste {test} - Entrada {entry} - {number_of_iterations} iterações \
    - Tempo de execução: {round(end - start, 8)} ms')
    return result


array1 = [1, 2, 3, 4, 5]

multiply_arrays(array1, array1, 1)
multiply_arrays(array1 * 2, array1 * 2, 2)
multiply_arrays(array1 * 3, array1 * 3, 3)

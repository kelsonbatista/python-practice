def insertion_sort(numbers):
    n = len(numbers)  # Quantidade de elementos na lista

    for index in range(1, n):  # Começaremos a ordenar pelo segundo elemento
        key = numbers[index]

        new_position = index - 1  # posição anterior para iniciar a comparação
        while new_position >= 0 and numbers[new_position] > key:
            numbers[new_position + 1] = numbers[new_position]  # elemento
            new_position = new_position - 1

        numbers[new_position + 1] = key  # Insere a chave na posição correta

    return numbers


numbers = [7, 5, 9, 2, 6, 8]
print(insertion_sort(numbers))

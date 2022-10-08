# A estrutura deve estar ordenada para que a busca binária funcione
# os índices podem ser no máximo iguais, o início não pode ultrapassar o fim
# encontro o meio
# ------------------------------------------------------------------------
# dividing two numbers in python is done using '/' and '//' operators
# 5 / 2 = 2.5
# using double forward slash results and integer if the answer is float
# 5 // 2 = 2
# ------------------------------------------------------------------------
# se o elemento do meio for o alvo, devolve a posição do meio
# se o elemento for menor, atualiza o índice do fim
# caso contrário, atualiza o índice do inicio
# Não encontrou? Retorna -1

def binary_search(numbers, target):
    # definir os índices
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            return mid
        if target < numbers[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


numbers = [2, 3, 4, 10, 40]
target = 40

result = binary_search(numbers, target)
print(f"Elemento encontrado na posição: {result}")

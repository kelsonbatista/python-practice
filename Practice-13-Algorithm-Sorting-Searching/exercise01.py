# Exercício 1 Dado um array com os seguintes elementos
# ["zebra", "macaco", "elefante", "arara", "javali"],
# após duas iterações utilizando bubble sort, como estaria este array?


def bubble_sort(animals):
    n = len(animals)
    for position in range(n - 1):
        for item in range(0, n - 1 - position):
            if animals[item] > animals[item + 1]:
                current = animals[item]
                animals[item] = animals[item + 1]
                animals[item + 1] = current
    return animals


animals = ["zebra", "macaco", "elefante", "arara", "javali"]
print(bubble_sort(animals))

# Exercício 14: Percorra a lista do exercício 13 e imprima
# "Múltiplo de 3" se o elemento for divisível por 3.

ratings = [6, 8, 5, 9, 10]

new_ratings2 = [10 * rating for rating in ratings]
print(new_ratings2, "<<<< new_ratings 2")

for value in new_ratings2:
    if value % 3 == 0:
        print(f"{value} <<<< multiplo de 3")

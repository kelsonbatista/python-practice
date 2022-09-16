# Exercício 5: Considere que a cobertura da tinta é de 1 litro
# para cada 3 metros quadrados e que a tinta é vendida em latas
# de 18 litros, que custam R$ 80,00. Crie uma função que retorne
# dois valores em uma tupla contendo a quantidade de latas de tinta
# a serem compradas e o preço total a partir do tamanho de uma parede(em m²).

def wall(area):
    can_price = 80
    can_size = 18
    required_liters = area / 3
    required_cans = required_liters // can_size
    price = required_cans * can_price
    if required_cans % can_size:
        required_cans += 1
        price += can_price
    return required_cans, price


print(wall(108))

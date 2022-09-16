# Exercício 4: Suponha que o preço de capa de um livro seja R$ 24,20,
# mas as livrarias recebem um desconto de 40%. O transporte custa 3,00
# para o primeiro exemplar e 75 centavos para cada exemplar adicional.
# Qual é o custo total de atacado para 60 cópias? Escreva uma
# expressão que receba o custo total e a imprima.

books = 60
p = 24.20
d = 0.4
tf = 3
tu = 0.75

price = p * (1 - d)
logistics = tf + ((books - 1) * tu)

total = books * (price + logistics)
print('R$', total, '<<<<<< total')

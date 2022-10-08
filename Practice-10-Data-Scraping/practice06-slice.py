# Recupera o primeiro elemento
print([1, 2, 3][0])  # Saída: 1

# Quando não incluso o valor inicial, iniciaremos do índice 0
# e do índice 2 em diante, os elementos não são incluídos
print((1, 2, 3, 4)[:2])  # Saída: (1, 2)

# Quando omitimos o valor final
# o fatiamento ocorre até o fim da sequência
print((1, 2, 3, 4)[1:])  # Saída: (2, 3, 4)

# Vá do índice 3 até o 7.
# O item no índice 7 não é incluído
print("palavra"[3:7])  # Saída: "avra"

# Começando do elemento de índice 1, vá até o último,
# saltando de 2 em 2
print([1, 2, 3, 4][1::2])  # Saída: [2, 4]

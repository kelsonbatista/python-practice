# Exercício 4: Um posto está vendendo combustíveis
# com a seguinte tabela de descontos:

# Álcool:
#   - Até 20 litros, desconto de 3% por litro;
#   - Acima de 20 litros, desconto de 5% por litro.
# Gasolina:
#   - Até 20 litros, desconto de 4% por litro;
#   - Acima de 20 litros, desconto de 6% por litro.

# Escreva uma função que receba o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma:
# A - álcool, G - gasolina), e retorne o valor a ser pago
# pelo cliente, sabendo-se que o preço do litro da gasolina
# é R$ 2,50, e o preço do litro do álcool é R$ 1,90.


def gas(liters, type):
    total = 0
    gas_price = 2.50
    etanol_price = 1.90
    if type == "G":
        if liters <= 20:
            total = liters * (gas_price * (1 - 0.04))
        else:
            total = liters * (gas_price * (1 - 0.06))
    else:
        if liters <= 20:
            total = liters * (etanol_price * (1 - 0.03))
        else:
            total = liters * (etanol_price * (1 - 0.05))
    print("R$ ", total)


gas(21, "G")

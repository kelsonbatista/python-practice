# Exercício 6: Crie uma função que receba os três lado de um
# triângulo e informe qual o tipo de triângulo formado ou "não
# é triangulo", caso não seja possível formar um triângulo.


def triangle(side1, side2, side3):
    if side1 + side2 > side3:
        print("é triângulo")
    else:
        print("não é triângulo")


triangle(30, 20, 50)

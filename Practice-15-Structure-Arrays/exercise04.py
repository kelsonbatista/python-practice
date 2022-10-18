# Exercício 4 Você têm dois arrays de números inteiros que
# representam: (I) instantes de entrada e saídas em uma biblioteca
# (II) um número que represente um instante a ser buscado.
# Retorne quantas pessoas estudantes estão na biblioteca naquele
# instante. Considere que todo estudante que entrou e saiu da biblioteca.


def students(arrival, departure, instance):
    result = 0
    for i in range(len(arrival)):
        if arrival[i] < instance < departure[i]:
            result += 1
    return result


entradas = [1, 2, 3, 2]
saidas = [3, 2, 7, 12]
instante_buscado = 4
# resultado: 1

# O estudante 1 entrou no instante 1 e saiu no 3, já o segundo entrou
# e saiu no 2 e o último foi único a estar presente no instante 4.

print(students(entradas, saidas, instante_buscado))

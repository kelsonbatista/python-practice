# Exercício 3: Dado um arquivo contendo estudantes e suas
# respectivas notas, escreva um programa que:
# 1. lê todas essas informações;
# 2. aplique um filtro, mantendo somente as pessoas que estão reprovadas;
# 3. escreva seus nomes em outro arquivo.

file = open("students.txt", mode="r")
output = open("students-output.txt", mode="w")
for line in file:
    if int(line.split()[1]) < 6:
        print(line.split()[0])
        output.writelines(f'{line.split()[0]}\n')
file.close()
output.close()

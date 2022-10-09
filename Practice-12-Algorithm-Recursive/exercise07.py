# Exercício 7: Escreva um algoritmo recursivo que resolva
# o problema da torre de hanoi, seguindo as instruções:
# Assim como na imagem abaixo, a torre deve conter 3 discos, e três colunas;
# Os discos começam alinhados na primeira coluna, e devem ser
# organizados respeitando a ordem de tamanho, na última coluna.


def hanoi_tower(discs, source, target, auxiliary):
    if discs == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi_tower(discs - 1, source, auxiliary, target)
    print(f"Move disk {discs} from {source} to {target}")
    hanoi_tower(discs - 1, auxiliary, target, source)


print(hanoi_tower(3, "A", "C", "B"))

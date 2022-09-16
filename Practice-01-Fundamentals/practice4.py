# Exercício 4: Crie uma função que receba uma lista de nomes e
# retorne o nome com a maior quantidade de caracteres. Por exemplo,
# para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"],
# o retorno deve ser "Fernanda".


def names(list):
    new_name = list[0]
    for name in list:
        if len(name) > len(new_name):
            new_name = name
    return new_name


list_names = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
print(names(list_names))

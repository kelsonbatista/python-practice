# Em seu terminal Python, crie uma lista (do conhecido tipo list)
# com alguns elementos. Agora, chame a função nativa iter(),
# passando essa lista como parâmetro, e veja que é retornado
# um objeto iterador do tipo list_iterator.


from rich import print


minha_lista = list([1, 2, 3, 4, 5])

list_iterator = iter(minha_lista)

print(list_iterator)

# Guarde este objeto iterador em uma variável e veja o que
# acontece quando chamar a função nativa next() passando
# esse objeto como parâmetro.

for item in minha_lista:
    print(next(list_iterator))

# Exercício 7: Um conjunto ou set pode ser inicializado utilizando-se
# também o método set(). Inicialize uma variável com essa função
# var = set() e adicione seu nome ao conjunto utilizando um dos métodos
# vistos acima. Depois, imprima a variável e confira
# se o retorno é: {'seu_nome'}.

# conjuntos (set) podem ser alterados

var = set()
var.add("Josh Smith")
print(var)

permissions = {"member", "group"}
# permissions.add("root")
# print(permissions)

# permissions.add("member")
# print(permissions)

# permissions.union({"user"})
# print(permissions)

permissions.intersection({"user", "member"})
print(permissions)

# permissions.difference({"user"})
# print(permissions)

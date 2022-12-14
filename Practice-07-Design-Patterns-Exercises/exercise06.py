# Exercício 6: Você está trabalhando em um sistema de orçamentos
# que faz cálculos de impostos e precisa ser refatorado para adicionar
# novos, que no caso são o PIS (0,65%) e o COFINS (3%). Mas durante
# a refatoração, você se depara com uma má prática de código.
# Encontre essa má prática e a solucione em conjunto com a refatoração.


from abc import ABC, abstractmethod


class OrcamentoStrategy(ABC):  # Interface
    @classmethod
    @abstractmethod
    def calcular(cls, valor):
        raise NotImplementedError


class ISSStrategy(OrcamentoStrategy):
    @classmethod
    def calcular(cls, valor):
        return f"ISS: {valor * 0.1}"


class ICMSStrategy(OrcamentoStrategy):
    @classmethod
    def calcular(cls, valor):
        return f"ICMS: {valor * 0.06}"


class PISStrategy(OrcamentoStrategy):
    @classmethod
    def calcular(cls, valor):
        return f"PIS: {valor * 0.0065}"


class CONFINSStrategy(OrcamentoStrategy):
    @classmethod
    def calcular(cls, valor):
        return f"CONFINS: {valor * 0.03}"


class Orcamento:
    def __init__(self, valor):
        self.valor = valor

    def calcular_imposto(self, imposto):
        return imposto.calcular(self.valor)


orcamento = Orcamento(1000)
print(orcamento.calcular_imposto(ISSStrategy))
print(orcamento.calcular_imposto(ICMSStrategy))
print(orcamento.calcular_imposto(PISStrategy))
print(orcamento.calcular_imposto(CONFINSStrategy))


# class Orcamento:
#     def __init__(self, valor):
#         self.valor = valor

#     def calcular_imposto(self, imposto):
#         if imposto == 'ISS':
#             return self.__calcular_iss()
#         elif imposto == 'ICMS':
#             return self.__calcular_icms()

#     def __calcular_iss(self):
#         return self.valor * 0.1

#     def __calcular_icms(self):
#         return self.valor * 0.06


# orcamento = Orcamento(1000)
# print(f"ISS: {orcamento.calcular_imposto('ISS')}")
# print(f"ICMS: {orcamento.calcular_imposto('ICMS')}")

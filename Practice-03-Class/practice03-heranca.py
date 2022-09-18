# Implemente a classe Microondas, Batedeira e Fogão, sempre
# herdando da classe Eletrodoméstico e para testar, instancie
# as novas classes e realize alguns prints, como por exemplo,
# divulgando o preço do Eletrodoméstico.

class Eletrodomestico:
    def __init__(self, cor, potencia, voltagem, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__voltagem = voltagem
        self.__preco = preco
        self.__ligado = False
        self.__amperagem = 0

    # getter
    @property
    def cor(self):
        return self.__cor

    # setter
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    def ligar(self, velocidade):
        self.__velocidade = velocidade
        self.__amperagem = (
          (self.__potencia / self.__voltagem) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def esta_desligado(self):
        return self.__ligado

    def __str__(self):
        return f"""
          Cor: {self.__cor}
          Potência: {self.__potencia}
          Voltagem: {self.__voltagem}
          Preço: {self.__preco}
        """


class Microondas(Eletrodomestico):  # Exemplo de Herança
    def __init__(self, cor, potencia, voltagem, preco, litros):
        # chamando o método da classe mãe
        super().__init__(cor, potencia, voltagem, preco)
        self.litros = litros

        def __str__(self):
            return f"""
              Litros: {self.litros}
            """


class Batedeira(Eletrodomestico):  # Exemplo de Herança
    def __init__(self, cor, potencia, voltagem, preco, capacidade):
        # chamando o método da classe mãe
        super().__init__(cor, potencia, voltagem, preco)
        self.capacidade = capacidade


class Fogao(Eletrodomestico):  # Exemplo de Herança
    def __init__(self, cor, potencia, voltagem, preco, bocas, forno):
        # chamando o método da classe mãe
        super().__init__(cor, potencia, voltagem, preco)
        self.bocas = bocas
        self.forno = forno


microondas = Microondas('Prata', '250W', '220V', '589.90', '20L')
print(microondas)

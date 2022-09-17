from bank_strategy import BancoStrategy


class ItauStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Código específico do Itau (exemplo)
        print("Débito realizado pelo Itau")

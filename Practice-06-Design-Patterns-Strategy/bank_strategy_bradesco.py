from bank_strategy import BancoStrategy


class BradescoStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Código específico do Bradesco (exemplo)
        print("Sucesso! Débito Bradesco!")

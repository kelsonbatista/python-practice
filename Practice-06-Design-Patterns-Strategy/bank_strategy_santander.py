from bank_strategy import BancoStrategy


class SantanderStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Código específico do Santander (exemplo)
        print("Santander, Débito efetuado!")

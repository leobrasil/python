from conta import Conta

class Poupanca(Conta):

    def __init__(self, n_conta, saldo=0):
        super().__init__(n_conta,saldo)
        self.taxa_juros = 0.005


    def metodo(self):
        print('metodo da classe poupanca')
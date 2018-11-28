class Conta():
    def __init__(self, num_conta, saldo=0):
        self.conta = num_conta
        self.saldo = saldo
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False
        
    def depositar(self,valor):
        if(valor >0):
            self.saldo+=valor

    
    def transferir(self,valor, conta):
        try:
            if not self.sacar(valor):
                raise ValueError("falha na transferencia")
            try:
                conta.depositar(valor)
            except AttributeError:
                print('Objeto destino nao possui o meotod depositar')
                #volta o dinheiro para a conta
                self.depositar(valor)
        except Exception as e:
            print('Erro: {}'.format(e))



c1 = Conta('1234455',500)
c2 = Conta('1234456',700)
print(c1.saldo)
c1.depositar(400)
print(c1.saldo)
c1.sacar(20)
print(c1.saldo)
c1.transferir(200,c2)
print('transferencia')
print(c1.saldo)
print(c2.saldo)
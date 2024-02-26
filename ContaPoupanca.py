import datetime

class Poupanca:
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneracaoConta(self):
        self.saldo += self.saldo * self.taxaremuneracao
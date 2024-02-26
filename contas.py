import datetime

from extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero 
        self.saldo = saldo 
        self.sata = abertura = datetime.datetime.today()
        self.extrato = Extrato()


    def depositar(self,valor):
        self.saldo += valor
        self.extrato.transacoes.append(["Deposito", valor,"Data",datetime.datetime.today()])

    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["Saque", valor,"Data",datetime.datetime.today()])
            return True
        
    def tranferenciaValor(self,contaDestino,valor):
        if self.saldo < valor:
            return ("Saldo insuficiente! ")
        else:   
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["Transferencia", valor,"Data",datetime.datetime.today()])
            return("Tranferencia realizada! ")
        
    def gerarsaldo(self):
        print(f"Numero:{self.numero}\n saldo: {self.saldo}")        

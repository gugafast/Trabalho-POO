from contas import Conta
from ContaPoupanca import Poupanca

class ContaRemuneraPoupanca(Conta, Poupanca):
    def __init__(self, taxaremuneracao, clientes, numero, saldo):
        Conta.__init__(self, clientes, numero, saldo)]
        Poupanca.__init__(self, taxaremuneracao)
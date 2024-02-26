from clientes import Cliente
from contas import Conta
from contaEspecial import ContaEspecial

cliente1 = Cliente("123","Joao","Rua X")
cliente2 = Cliente ("456","Maria","Rua W")
cliente3 = Cliente("789","Joana","Rua Y")
conta1 = Conta([cliente1,cliente2],1,2000)
conta2 = ContaEspecial([cliente3],3,1000,2000)
conta2.depositar(100)
conta2.sacar(2000)

conta2.extrato.extrato(conta2.numero)
# Programa de Sistema Bancário / Poo

# class Conta:
class Conta:
    def __init__(self, nomeTitular, cpf, saldo):
        self.nomeTitular = nomeTitular
        self.cpf = cpf
        self.saldo = saldo


    def deposito(self, valor):
        self.saldo += valor


    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False


    def transfere(self, destino, valor):
        if self.saldo < valor:
            return ("Você nao tem saldo para tranferencia!")
        else:
            destino.deposito(valor)
            self.saldo -= valor
            return ("Transferencia realizada com sucesso!")


    def extrato(self):
        print("-"*50)
        print(f" Nome do titular da conta: {self.nomeTitular}\n CPF do titular: {self.cpf}\n Saldo do titular: R$ {self.saldo:.2f}")
        print("-"*50)


conta1 = Conta("jose", 79799797979, 2000)
conta2 = Conta("Carlos", 232342342343,100)


print(conta1.transfere(conta2, 500))


'''conta1.deposito(1000)


valor_saque = 1000
resultado_saque = conta1.sacar(valor_saque)
if resultado_saque:
    print(f"Saque de R$ {valor_saque} Realizado com sucesso! ")
else:
    print("Você nao possue saldo suficiente para este saque!")'''


conta1.extrato()
conta2.extrato()
    


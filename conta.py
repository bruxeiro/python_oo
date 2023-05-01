class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objeto{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        if valor <= 0:
            print("Digite um valor acima de 0")
        else:
            self.__saldo += valor
            self.extrato()

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor > valor_disponivel
    def saca(self, valor):
        if self.__pode_sacar(valor):
            print("Digite um valor menor do que o saldo e limite")
        else:
            self.__saldo -= valor
            self.extrato()

    def transfere(self, valor, acc):
        if valor > self.__saldo:
            print("Digite um valor menor do que o saldo")
        else:
            self.saca(valor)
            acc.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

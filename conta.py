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

    def saca(self, valor):
        if valor > self.__saldo:
            print("Digite um valor menor do que o saldo")
        else:
            self.__saldo -= valor
            self.extrato()

class Data:
    def __init__(self, dia, mes, ano):
        print("Contruindo objeto{}".format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatdata(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))



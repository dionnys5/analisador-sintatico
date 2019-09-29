class TerminaisDigitos(dict):
    def __init__(self):
        super().__init__()
        self.__dict__ = self
        self.eh_terminal = True
        self.valor = None
        self.valores_possiveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def inserir(self, valor):
        if valor in self.valores_possiveis:
            self.valor = valor
            return True
        return False


class NoBarra(dict):
    def __init__(self):
        super().__init__()
        self.__dict__ = self
        self.eh_terminal = True
        self.valores_possiveis = ['/']
        self.valor = None

    def inserir(self, valor):
        if valor in self.valores_possiveis:
            self.valor = valor
            return True
        return False


class NoNumero(dict):
    def __init__(self):
        super().__init__()
        self.__dict__ = self
        self.eh_terminal = False
        self.valor = None

    def inserir(self, valor):
        if self.valor is None:
            self.valor = TerminaisDigitos()
            self.valor.inserir(valor)
            if self.valor:
                return True
        return False


class NoDia(dict):
    def __init__(self):
        super().__init__()
        self.__dict__ = self
        self.eh_terminal = False
        self.primeiro = None
        self.segundo = None

    def inserir(self, valor):
        if self.primeiro is None:
            self.primeiro = NoNumero()
            self.primeiro.inserir(valor)
            if self.primeiro:
                return True
        elif self.segundo is None:
            self.segundo = NoNumero()
            self.segundo.inserir(valor)
            if self.segundo:
                return True
        return False


class NoMes(dict):
    def __init__(self):
        super().__init__()
        self.__dict__ = self
        self.eh_terminal = False
        self.primeiro = None
        self.segundo = None

    def inserir(self, valor):
        if self.primeiro is None:
            self.primeiro = NoNumero()
            self.primeiro.inserir(valor)
            if self.primeiro:
                return True
        elif self.segundo is None:
            self.segundo = NoNumero()
            self.segundo.inserir(valor)
            if self.segundo:
                return True
        return False


class NoAno(dict):
    def __init__(self):
        super().__init__()
        self.__dict__ = self
        self.eh_terminal = False
        self.primeiro = None
        self.segundo = None
        self.terceiro = None
        self.quarto = None

    def inserir(self, valor):
        if self.primeiro is None:
            self.primeiro = NoNumero()
            self.primeiro.inserir(valor)
            if self.primeiro:
                return True
        elif self.segundo is None:
            self.segundo = NoNumero()
            self.segundo.inserir(valor)
            if self.segundo:
                return True
        elif self.terceiro is None:
            self.terceiro = NoNumero()
            self.terceiro.inserir(valor)
            if self.terceiro:
                return True
        elif self.quarto is None:
            self.quarto = NoNumero()
            self.quarto.inserir(valor)
            if self.quarto:
                return True
        return False


class NoRaizData(dict):
    def __init__(self):
        super().__init__()
        self.__dict__ = self
        self.eh_terminal = False
        self.dia = NoDia()
        self.barra = NoBarra()
        self.mes = NoMes()
        self.barra2 = NoBarra()
        self.ano = NoAno()

    def inserir(self, valor):
        if self.dia.primeiro is None or self.dia.segundo is None:
            self.dia.inserir(valor)
        elif self.barra.valor is None:
            self.barra.inserir(valor)
        elif self.mes.primeiro is None or self.mes.segundo is None:
            self.mes.inserir(valor)
        elif self.barra2.valor is None:
            self.barra2.inserir(valor)
        elif self.ano.primeiro is None \
            or self.ano.segundo is None \
            or self.ano.terceiro is None \
            or self.ano.quarto is None:
            self.ano.inserir(valor)
        return False

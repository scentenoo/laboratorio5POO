from Progresion import progresion

class Aritmetica(progresion):
    def __init__(self, incremento, inicio):
        super().__init__(inicio)
        self.incremento = incremento

    def avanzar(self):
        self.start += self.incremento
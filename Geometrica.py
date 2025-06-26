from Progresion import progresion

class Geometrica(progresion):
    def __init__(self, base, inicio):
        super().__init__(inicio)
        self.base = base
    
    def avanzar(self):
        self.valor *= self.base
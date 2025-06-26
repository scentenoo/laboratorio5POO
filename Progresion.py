from abc import ABC, abstractclassmethod

class progresion(ABC):
    def __init__(self, start):
        self.start = start

    def sigValor(self):
        temp = self.valor
        self.avanzar()
        return temp
    
    def imprimirP(self, n):
        for _ in range(n):
            print(self.sigValor(), end=' ')
        print()

    @abstractclassmethod
    def avanzar(self):
        pass
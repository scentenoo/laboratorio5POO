from abc import ABC, abstractmethod

class progresion(ABC):
    def __init__(self, start):
        self.start = start

    def sigValor(self):
        temp = self.start
        self.avanzar()
        return temp
    
    def imprimirP(self, n):
        for _ in range(n):
            print(self.sigValor(), end=' ')
        print()

    @abstractmethod
    def avanzar(self):
        pass
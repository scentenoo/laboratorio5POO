from Progresion import progresion

class Fibonacci(progresion):
    def __init__(self):
        super().__init__(0)
        self.prev=1
    
    def avanzar(self):
        temp = self.prev
        self.prev = self.start
        self.start = temp
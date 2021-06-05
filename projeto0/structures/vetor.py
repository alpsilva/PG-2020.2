class Vetor:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    # Igualdade entre vetores.
    def __eq__(self, outro):
        return self.x1 == outro.x1 and self.x2 == outro.x2 and self.x3 == outro.x3

    # Multiplicacao por numero real.
    def __mul__(self, num):
        return Vetor(self.x1 * num, self.x2 * num, self.x3 * num)
    
    # Adicao entre vetores.
    def __add__(self, outro):
        return Vetor(self.x1 + outro.x1, self.x2 + outro.x2, self.x3 + outro.x3)
    
    # Subtracao entre vetores.
    def __sub__(self, outro):
        return Vetor(self.x1 - outro.x1, self.x2 - outro.x2, self.x3 - outro.x3)

    def print(self):
        print(self.x1, self.x2, self.x3)
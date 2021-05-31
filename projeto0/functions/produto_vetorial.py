from structures.vetor import Vetor

def produtoVetorial(vetor1, vetor2):
    x1 = (vetor1.x2 * vetor2.x3) - (vetor1.x3 * vetor2.x2)
    x2 = (vetor1.x3 * vetor2.x1) - (vetor1.x1 * vetor2.x3)
    x3 = (vetor1.x1 * vetor2.x2) - (vetor1.x2 * vetor2.x1)
    vetor3 = Vetor(x1, x2, x3)
    return vetor3
from structures.vetor import Vetor
from functions.norma import norma

def normalize(vetor):
    n = norma(vetor)
    vetorNormalizado = Vetor((vetor.x1/n), (vetor.x2/n), (vetor.x3/n))
    return vetorNormalizado
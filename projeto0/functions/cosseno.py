from functions.produto_escalar import produtoEscalar
from functions.norma import norma

def cosseno(vetor1, vetor2):
    produtoInterno = produtoEscalar(vetor1, vetor2)
    angulo = produtoInterno / (norma(vetor1) * norma(vetor2))
    return angulo
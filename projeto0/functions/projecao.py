import math
from structures.vetor import Vetor
from functions.norma import norma
from functions.produto_escalar import produtoEscalar

def projecao(vetor1, vetor2):
    pe = produtoEscalar(vetor1, vetor2)
    nq = math.pow(norma(vetor2), 2)
    l = pe / nq
    #l é o número real 'lambda' que ao multiplicar vetor2, gera a componente do vetor1 que será a projeção.
    vetor3 = Vetor(vetor2.x1 * l, vetor2.x2 * l, vetor2.x3 * l)
    return vetor3
    #vetor3 é o vetor projeção do vetor1 no vetor2
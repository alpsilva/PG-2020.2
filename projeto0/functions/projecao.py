import math
from structures.vetor import Vetor
from functions.norma import norma
from functions.produto_escalar import produtoEscalar

def projecao(vetor1, vetor2):
    #Atenção: Essa função deve projetar o vetor1 no vetor2, mas a função do symbolab recebe a ordem ao contrário.
    #Porém, acredito que está correto.
    pe = produtoEscalar(vetor1, vetor2)
    nq = math.pow(norma(vetor2), 2)
    l = pe / nq
    #l é o número real 'lambda' que ao multiplicar vetor2, gera a componente do vetor1 que será a projeção.
    vetor3 = Vetor(vetor2.x1 * l, vetor2.x2 * l, vetor2.x3 * l)
    return vetor3
    #vetor3 é o vetor projeção do vetor1 no vetor2
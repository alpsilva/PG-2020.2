import math
from structures.vetor import Vetor
from functions.produto_escalar import produtoEscalar

# vetor1 e vetor2 são vetores
# o retorno é o vetor-reflexão do vetor1 em relação ao vetor2
def reflexao(vetor1, vetor2):
    return (vetor2 * (2.0 * produtoEscalar(vetor2, vetor1))) - vetor1
    
from structures.vetor import Vetor
from structures.base import Base

# simPy apenas para a forma escada, que nao esta no escopo do projeto.
from sympy import *

# v = (x, y, z)

# a * x1 + b * x2 + c * x3 = x
# a * y1 + b * y2 + c * y3 = y
# a * z1 + b * z2 + c * z3 = z

# descobrir (a, b, c) é descobrir o vetor na base nova. (x, y, z) eh o que ja temos

# eh preciso escalonar a matriz. lucio disse na monitoria que pode usar algoritmos prontos.


def mudebase(vetor, base):
    v1 = Vetor(base.v1)
    v2 = Vetor(base.v2)
    v3 = Vetor(base.v3)

    formaEscada = sympy.Matrix([[v1.x1, v1.x2, v1.x3, vetor.x1], [v2.x1, v2.x2, v2.x3, vetor.x2], [v3.x1, v3.x2, v3.x3, vetor.x3]])
    #sympy.Matrix.rref() retorna dois objetos: A matriz e os index dos pivos. so precisamos da matriz
    formaEscada = formaEscada.Matrix

    # calculo c
    c = formaEscada[2, 3] / formaEscada[2, 2]

    # calculo b
    b = formaEscada[1, 3] - (formaEscada[1, 2] * c) / formaEscada[1, 1]

    #calculo a
    a = formaEscada[0, 3] - (formaEscada[0, 2] * c) - (formaEscada[0, 1] * b) / formaEscada[0, 0]

    return [a, b, c]
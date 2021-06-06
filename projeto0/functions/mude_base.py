from structures.vetor import Vetor
from structures.base import Base

# NumPy apenas para função inverse, que não está no escopo do projeto.
import numpy as np


def mudebase(vetor, base):
    # assume a base canonica como base do vetor e utiliza a outra funcao de mudanca de base
    b2 = np.array([[base.v1.x1, base.v1.x2, base.v1.x3], [base.v2.x1, base.v2.x2, base.v2.x3], [base.v3.x1, base.v3.x2, base.v3.x3]])
    v_b1 = np.array([vetor.x1, vetor.x2, vetor.x3])
    v_b2 = np.linalg.inv(b2) @ v_b1
    return [v_b2[0], v_b2[1], v_b2[2]]
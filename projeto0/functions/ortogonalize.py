from functions.norma import norma
from functions.projecao import projecao
from structures.base import Base

def ortogonalize (base):
    v1 = base.v1
    v2 = base.v2
    v3 = base.v3

    # Processo de Gram–Schmidt
    u1 = v1
    e1 = u1 / norma(u1)

    u2 = v2 - projecao(v2, u1)
    e2 = u2 / norma(u2)

    u3 = v3 - projecao(v3, u1) - projecao(v3, u2)
    e3 = u3 / norma(u3)

    baseOrtoganilizada = Base(e1, e2, e3)
    return baseOrtoganilizada
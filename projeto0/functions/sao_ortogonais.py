from functions.produto_escalar import produtoEscalar

def saoOrtogonais(vetor1, vetor2):
    # vetor1 é ortogonal a vetor2 se o produto escalar entre eles for igual a 0.
    pe = produtoEscalar(vetor1, vetor2)
    b = (pe == 0)
    return b
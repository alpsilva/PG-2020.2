from functions.produto_escalar import produtoEscalar

def eOrtogonal(reta, vetor):
    pe = produtoEscalar(reta.vetorDiretor, vetor)
    b = (pe == 0)
    return b
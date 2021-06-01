from functions.produto_vetorial import produtoVetorial

def eParalelo(reta, vetor):
    pv = produtoVetorial(reta.vetorDiretor, vetor)
    b = (pv.x1 == 0) and (pv.x2 == 0) and (pv.x3 == 0)
    
    return b
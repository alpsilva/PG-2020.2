from functions.e_paralelo import eParalelo

def saoComplementosOrtogonais(reta, plano):
    b = eParalelo(reta, plano.vetorNormal)
    return b

def saoComplementosOrtogonaisPlanoReta(plano, reta):
    b = eParalelo(reta, plano.vetorNormal)
    return b
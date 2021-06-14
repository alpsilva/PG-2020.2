from functions.projecao import projecao

def componenteOrtogonal(vetor, plano):
    # projeta o vetor no vetorNormal do plano
    vetorProjetado = projecao(vetor, plano.vetorNormal)
    return vetorProjetado
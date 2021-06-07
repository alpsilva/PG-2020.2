from structures.vetor import Vetor
from functions.sao_paralelos import saoParalelos

def eLI(arrayVetores):

    # para ser LI nao pode haver paralelismo entre nenhuma combinação dos vetores. Se ouver ao menos 1, nao e LI.
    if(len(arrayVetores) == 2):
        vetor1 = arrayVetores[0]
        vetor2 = arrayVetores[1]
        possui_paralelismo = saoParalelos(vetor1, vetor2)
    else:
        vetor1 = arrayVetores[0]
        vetor2 = arrayVetores[1]
        vetor3 = arrayVetores[2]
        possui_paralelismo = saoParalelos(vetor1, vetor2) or saoParalelos(vetor1, vetor3) or saoParalelos(vetor2, vetor3)

    # se possui paralelismo, retorna false
    return not possui_paralelismo
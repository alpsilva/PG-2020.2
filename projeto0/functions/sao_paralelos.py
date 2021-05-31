from functions.produto_vetorial import produtoVetorial

def saoParalelos(vetor1, vetor2):
    #vetor1 é paralelo a vetor2 se eles são escalares múltiplos um do outro
    #ou seja, se vetor1 = t * vetor2, onde t é um numero qualquer
    #também é possível determinar paralelismo se o produto vetorial deles for 0
    
    #método 1
    #div1 = vetor1.x1 / vetor2.x1
    #div2 = vetor1.x2 / vetor2.x2
    #div3 = vetor1.x3 / vetor2.x3
    #b = (div1 == div2) and (div1 == div3)
    
    #método 2
    pv = produtoVetorial(vetor1, vetor2)
    b = (pv.x1 == 0) and (pv.x2 == 0) and (pv.x3 == 0)

    return b
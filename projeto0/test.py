# classes
from math import cos, frexp
from structures.vetor import Vetor

# functions
from functions.produto_escalar import produtoEscalar
from functions.norma import norma
from functions.normalize import normalize
from functions.cosseno import cosseno
from functions.projecao import projecao
from functions.produto_vetorial import produtoVetorial

#teste das classes de vetores
v1 = Vetor(2, 3, 2)
v2 = Vetor(3, 2, 3)
v1.print()
v2.print()

#teste da função produtoEscalar
produto_escalar = produtoEscalar(v1, v2)
print(produto_escalar)

#teste da função norma
norma_v1 = norma(v1)
norma_v2 = norma(v2)
print(norma_v1)
print(norma_v2)

#teste da função normalize
v1_normalizado = normalize(v1)
v2_normalizado = normalize(v2)
v1_normalizado.print()
v2_normalizado.print()

#teste da função cosseno
cosseno_v1_v2 = cosseno(v1, v2)
print(cosseno_v1_v2)

#teste da função projecao
projecao_v1_v2 = projecao(v1, v2)
projecao_v1_v2.print()

#teste da função produtoVetorial
produto_vetorial = produtoVetorial(v1, v2)
produto_vetorial.print()
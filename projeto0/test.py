# classes
from math import cos, frexp
from structures.vetor import Vetor

# functions
from functions.produto_escalar import produtoEscalar
from functions.norma import norma
from functions.normalize import normalize
from functions.cosseno import cosseno

v1 = Vetor(2, 3, 2)
v2 = Vetor(3, 2, 3)
print(v1.x1, v1.x2, v1.x3)
print(v2.x1, v2.x2, v2.x3)

produto_escalar = produtoEscalar(v1, v2)
print(produto_escalar)

norma_v1 = norma(v1)
norma_v2 = norma(v2)
print(norma_v1)
print(norma_v2)

v1_normalizado = normalize(v1)
v2_normalizado = normalize(v2)
print(v1_normalizado.x1, v1_normalizado.x2, v1_normalizado.x3)
print(v2_normalizado.x1, v2_normalizado.x2, v2_normalizado.x3)

cosseno_v1_v2 = cosseno(v1, v2)
print(cosseno_v1_v2)
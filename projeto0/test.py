
#import de classes
from structures.vetor import Vetor
from structures.ponto import Ponto
from structures.reta import Reta
from structures.plano import Plano
from structures.base import Base

#import de functions
from functions.produto_escalar import produtoEscalar
from functions.norma import norma
from functions.normalize import normalize
from functions.cosseno import cosseno
from functions.projecao import projecao
from functions.produto_vetorial import produtoVetorial
from functions.reflexao import reflexao
from functions.sao_paralelos import saoParalelos
from functions.sao_ortogonais import saoOrtogonais
from functions.e_li import eLI

from functions.diretor import diretor
from functions.normal import normal
from functions.e_paralelo import eParalelo
from functions.e_ortogonal import eOrtogonal
from functions.projecao import projecao
from functions.componente_ortogonal import componenteOrtogonal

from functions.ortogonalize import ortogonalize
from functions.mude_base import mudebase

#teste das classes de vetores
v1 = Vetor(2, 3, 2)
v2 = Vetor(3, 2, 3)
v1.print()
v2.print()

#teste dos metodos basicos da classe de vetor
assert Vetor(1, 2, 3) == Vetor(1, 2, 3)
assert Vetor(1, 3, 4) != Vetor(1, 1, 1)
print('Igualdade entre vetores OK.')
assert Vetor(1, 2, 3) * 2 == Vetor(2, 4, 6)
assert Vetor(1, 2, 3) * 1 == Vetor(1, 2, 3)
print('Produto de vetor por escalar OK.')
assert Vetor(1, 2, 3) + Vetor(3,2,1) == Vetor(4, 4, 4)
print('Soma de vetores OK')
assert Vetor(1, 2, 3) - Vetor(1, 2, 3) == Vetor(0, 0, 0)
print('Subtracao de vetores OK')

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

#teste da função reflexão
vref1 = Vetor(1,0,0)
vref2 = Vetor(0,1,0)
reflexao = reflexao(vref1, vref2)
print('Reflexao:')
reflexao.print()

#teste da função saoParalelos
b = saoParalelos(v1, v2)
print("v1 e v2 são paralelos? ", b)

v3 = Vetor(5, 5, 5)
v4 = Vetor(10, 10, 10)
b2 = saoParalelos(v3, v4)
print("v3 e v4 são paralelos? ", b2)

#teste da função saoOrtogonais
b = saoOrtogonais(v1, v2)
print("v1 e v2 são ortogonais? ", b)

v5 = Vetor(-5, 1, 1)
v6 = Vetor(1, 2, 3)
b2 = saoOrtogonais(v5, v6)
print("v5 e v6 são ortogonais? ", b2)

#teste da função eLI
array1 = [v3, v4]
b3 = eLI(array1)
print("v3 e v4 são LI? ", b3)

v7 = Vetor(3, 5, 7)
v8 = Vetor(11, 13, 17)
v9 = Vetor(19, 23, 29)
array2 = [v7, v8, v9]
b4 = eLI(array2)
print("v7, v8 e v9 são LI? ", b4)

#teste da funcao diretor
pnt = Ponto(0, 0, 0)
r1 = Reta(pnt, v6)
d = diretor(r1)
d.print()

#teste da funcao normal
pln = Plano(pnt, v3)
n = normal(pln)
n.print()

#teste da funcao eParalelo
r2 = Reta(pnt, v3)
print("a reta r2 e paralela ao vetor v6?", eParalelo(r2, v6))
print("a reta r2 e paralela ao vetor v4?", eParalelo(r2, v4))

#teste da funcao eOrtogonal
r3 = Reta(pnt, v5)
print("a reta r3 e ortogonal ao vetor v4?", eOrtogonal(r3, v4))
print("a reta r2 e ortogonal ao vetor v6?", eOrtogonal(r3, v6))

#teste da função projecao

#teste da funcao componente ortogonal
vetorNormalPlano = Vetor (5, 5, 5)
pontoPlano = Ponto(0, 0, 0)
plano = Plano(pontoPlano, vetorNormalPlano)
vetorOrtogonalPlano = Vetor(5, 5, 3)

vetorComponenteOrtogonal = componenteOrtogonal(vetorOrtogonalPlano, plano)

#teste da função ortogonalize
vb1 = Vetor(1, 0, 0)
vb2 = Vetor(1, 2, 0)
vb3 = Vetor(0, 2, 2)
base = Base(vb1, vb2, vb3)
baseOrtogonalizada = ortogonalize(base)
baseOrtogonalizada.print()

#teste da funcao mudeBase
# TODO ESSE BLOCO TA ERRADO

v_aux1 = Vetor(1, 0, 1)
v_aux2 = Vetor(1, 1, 0)
v_aux3 = Vetor(2, 2, -3)
base1 = Base(v_aux1, v_aux2, v_aux3)

v1 = Vetor(1, 0, 0)
v2 = Vetor(0, 1, 0)
v3 = Vetor(0, 0, 1)

# da base canonica para base 1
new_coord = mudebase(v1, base1)
print(new_coord[0], new_coord[1], new_coord[2])
new_coord = mudebase(v2, base1)
print(new_coord[0], new_coord[1], new_coord[2])
new_coord = mudebase(v3, base1)
print(new_coord[0], new_coord[1], new_coord[2])
# TODO ESSE BLOCO TA ERRADO
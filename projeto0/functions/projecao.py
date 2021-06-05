import math
from structures.vetor import Vetor
from functions.norma import norma
from functions.produto_escalar import produtoEscalar
from structures.reta import Reta
from structures.plano import Plano

def projecao(vetor, obj):
    
    if type(obj) is Vetor:
        #projecao(vetor1, vetor2)
        #Atenção: Essa função deve projetar o vetor1 no vetor2, mas a função do symbolab recebe a ordem ao contrário.
        #Porém, acredito que está correto.
        pe = produtoEscalar(vetor, obj)
        nq = math.pow(norma(obj), 2)
        l = pe / nq
        #l é o número real 'lambda' que ao multiplicar vetor2, gera a componente do vetor1 que será a projeção.
        vetorProjetado = Vetor(obj.x1 * l, obj.x2 * l, obj.x3 * l)
        #vetor3 é o vetor projeção do vetor1 no vetor2
    elif type(obj) is Reta:
        # projecao(vetor, reta)
        # n sei se esta certo, verifiquem
        pe = produtoEscalar(vetor, obj.vetorDiretor)
        nq = math.pow(norma(obj.vetorDiretor), 2)
        l = pe / nq
        vetorProjetado = Vetor(obj.vetorDiretor.x1 * l, obj.vetorDiretor.x2 * l, obj.vetorDiretor.x3 * l)
        
    elif type(obj) is Plano:
        # projecao(vetor, plano)
        vetorProjetado = "placeholder"
        
    return vetorProjetado
from structures.plano import Plano
from structures.reta import Reta

def formaCartesiana(obj):
    if type(obj) is Plano:
        # formaCartesiana(plano)
        a = obj.vetorNormal.x1
        b = obj.vetorNormal.x2
        c = obj.vetorNormal.x3
        d = obj.ponto.x1 + obj.ponto.x2 + obj.ponto.x3
        
        return [a, b, c, d]
    
    elif type(obj) is Reta:
        # formaCartesiana(reta)
        
        a = obj.vetorDiretor.x2/obj.vetorDiretor.x1
        b = -1
        c = 0
        d = obj.ponto.x2 - (a * obj.ponto.x1)
        
        e = 0
        f = obj.vetorDiretor.x3/obj.vetorDiretor.x2
        g = -1
        h = obj.ponto.x3 - (e * obj.ponto.x2)
        
        return [[a, b, c, d], [e, f, g, h]]
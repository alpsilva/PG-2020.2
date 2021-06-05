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
        
        return [[a, b, c, d], [e, f, g, h]]
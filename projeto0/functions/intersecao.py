from structures.plano import Plano
from functions.sao_paralelos import saoParalelos
from functions.forma_cartesiana import formaCartesiana
from structures.reta import Reta
from functions.sao_ortogonais import saoOrtogonais
from structures.esfera import Esfera
from structures.triangulo import Triangulo

def intersecao(obj1, obj2):
    if obj1 is Plano:
        # intersecao(plano1, plano2)
        
        if not saoParalelos(obj1.vetorNormal, obj2.vetorNormal):
            a = formaCartesiana(obj1)
            b = formaCartesiana(obj2)
            
            # agora eh necessario obter o ponto e vetor diretor a partir da forma cartesiana da reta
            
            return "placeholder"
        
    elif obj2 is Plano:
        # intersecao(reta, plano)
        
        [a, b, c, d] = formaCartesiana(obj2)
        
        if not saoOrtogonais(obj1.vetorDiretor, obj2.vetorNormal):
            # a reta intercepta o plano em apenas um ponto
            return "placeholder"
        
        elif a*obj1.ponto.x1 + b*obj1.ponto.x2 + c*obj1.ponto.x3 == d:
            # a reta está contida no plano
            return obj1
        
    elif obj2 is Reta:
        # intersecao(reta1, reta2)
        
        [[a, b, c, d], [e, f, g, h]] = formaCartesiana(obj2)
        
        return "placeholder"
    
    elif obj2 is Esfera:
        return "placeholder"
    
    elif obj2 is Triangulo:
        return "placeholder"    
        
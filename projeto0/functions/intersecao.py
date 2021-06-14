from functions.sao_paralelos import saoParalelos
from functions.forma_cartesiana import formaCartesiana
from structures.plano import Plano
from structures.ponto import Ponto
from structures.reta import Reta
from structures.vetor import Vetor
from structures.esfera import Esfera
from structures.triangulo import Triangulo
from functions.sao_ortogonais import saoOrtogonais
from functions.produto_escalar import produtoEscalar
from functions.e_paralelo import eParalelo

def intersecao(obj1, obj2):
    if type(obj1) is Plano:
        # intersecao(plano1, plano2)
        
        if not saoParalelos(obj1.vetorNormal, obj2.vetorNormal):
            a = formaCartesiana(obj1)
            b = formaCartesiana(obj2)
            
            # agora eh necessario obter o ponto e vetor diretor a partir da forma cartesiana da reta
            
            return "placeholder"
        
    elif type(obj2) is Plano:
        # intersecao(reta, plano)
        print("eh reta plano")
        [a,b, c, d] = formaCartesiana(obj2)

        if(produtoEscalar(obj1.vetorDiretor, obj2.vetorNormal) == 0):
            if(a*obj1.ponto.x + b*obj1.ponto.y + c*obj1.ponto.z + d == 0):
                return obj1
            else:
                return None

        t = (-1 * (a * obj1.ponto.x1 + b * obj1.ponto.x2 + c * obj1.ponto.x3 + d)) / ( a * obj1.vetorDiretor.x1 + b * obj1.vetorDiretor.x2 + c * obj1.vetorDiretor.x3)

        return Ponto(obj1.ponto.x1 + t * obj1.vetorDiretor.x1, obj1.ponto.x2 + t * obj1.vetorDiretor.x2, obj1.ponto.x3 + t * obj1.vetorDiretor.x3)
        
    elif type(obj2) is Reta:
        # intersecao(reta1, reta)
        formaCartesiana2 = formaCartesiana(obj2)

        v1 = Vetor(obj1.ponto.x1, obj1.ponto.x2, obj1.ponto.x3)
        v2 = Vetor(formaCartesiana2[0][0], formaCartesiana2[0][1], formaCartesiana2[0][2])
        v3 = Vetor(formaCartesiana2[1][0], formaCartesiana2[1][1], formaCartesiana2[1][2])

        produto1 = produtoEscalar(v1, v2) #(p, q, r)*(a, b, c)
        produto2 = produtoEscalar(v1, v3) #(p, q, r)*(e, f, g)
        produto3 = produtoEscalar(obj1.vetorDiretor, v2) #(x, y, z)*(a, b, c)
        produto4 = produtoEscalar(obj1.vetorDiretor, v3) #(x, y, z)*(e, f, g)

        t1 = (produto1 + formaCartesiana2[0][3]) / produto3
        t2 = (produto2 + formaCartesiana2[1][3]) / produto4

        if t1 == t2: #Se t1 == t2, então existe interseção
            if eParalelo(obj2, obj1.vetorDiretor):
                return v1
            else:
                x = obj1.ponto.x1 + (obj1.vetorDiretor.x1 * t1)
                y = obj1.ponto.x2 + (obj1.vetorDiretor.x2 * t1)
                z = obj1.ponto.x3 + (obj1.vetorDiretor.x3 * t1)
                return Ponto(x, y, z)
        else:
            return None
    
    elif type(obj2) is Esfera:
        return "placeholder"
    
    elif type(obj2) is Triangulo:
        return "placeholder"    
        
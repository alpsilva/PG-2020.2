# Checklist

## ESTRUTURAS

Ponto(x1, x2, x3) [x]  
x1, x2,x3 pertencentes aos reais  
  
-> Vetor(x1, x2 x3) [x]  
x1, x2, x3 pertencentes aos reais  
  
-> Segmento(ponto1, ponto2) [x]  
ponto1 e ponto2 são pontos que representam as extremidades do seguimento de reta  
  
-> Reta(ponto, vetorDiretor) [x]  
ponto é um ponto pertencendo à reta  
vetorDiretor é o vetor diretor da reta paramétrica  
  
-> Plano(ponto, vetorNormal) [x]  
ponto é um ponto pertencendo ao plano  
vetorNormal é um vetor normal ao plano  
  
-> Esfera(centro, raio) [x]  
centro é um ponto que representa o centro da esfera  
raio é um valor real que representa o módulo do raio da esfera  
  
-> Triangulo(ponto1, ponto2, ponto3) [x]  
ponto1, ponto2 e ponto3 são pontos que representam os vértices do triângulo
  
-> Base(v1, v2, v3) [x]  
v1, v2, v3 são vetores que formam uma base (tendo de ser linearmente independentes)  

## Funções

### Ferramentas básicas

-> produtoEscalar(vetor1, vetor2) => n; []  
vetor1 e vetor2 sendo dois vetores  
n sendo o valor do produto escalar entre vetor1 e vetor2  
  
-> norma(vetor) => n; []  
vetor é um vetor  
n é um número real que representa a norma desse vetor  
  
-> normalize(vetor) => vetorNormalizado; []  
vetor é um vetor  
vetorNomalizado é o vetor normalizado  
  
-> cosseno(vetor1, vetor2) => angulo; []  
vetor1 e vetor2 são vetores  
angulo é um número real que representa o ângulo em radianos  
  
-> projecao(vetor1, vetor2) => vetor3; []  
vetor1 e vetor2 são vetores  
vetor3 é o vetor-projeção do vetor1 no vetor2  
  
-> produtoVetorial(vetor1, vetor2) => vetor3; []  
vetor1 e vetor2 são vetores  
vetor3 é o vetor resultante do produto vetorial de vetor1 com vetor2  
  
-> reflexao(vetor1, vetor2) => vetor3; []  
vetor1 e vetor2 são vetores  
vetor3 é o vetor-reflexão do vetor1 em relação ao vetor3  
  
-> saoParalelos(vetor1, vetor2) => boolean; []  
vetor1 e vetor2 são vetores  
boolean é um valor booleano que afirma ou nega se o vetor1 é paralelo ao vetor2  
  
-> saoOrtogonais(vetor1, vetor2) => boolean; []  
vetor1 e vetor2 são vetores  
boolean é um valor booleano que afirma ou nega se vetor1 e vetor2 são ortogonais entre si  
  
-> eLI([vetor1, ..., vetorn]) => boolean; []  
[vetor1, vetor2, vetor3] é um array de três vetores
boolean é um valor booleano que afirma ou nega se vetor1, vetor2 e vetor3 são Linearmente Independentes  
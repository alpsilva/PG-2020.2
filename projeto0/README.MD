# Checklist

## ESTRUTURAS

- [x] `Ponto(x1, x2, x3)`
x1, x2,x3 pertencentes aos reais  
  
- [x] `Vetor(x1, x2 x3)`
x1, x2, x3 pertencentes aos reais  
  
- [x] `Segmento(ponto1, ponto2)`
ponto1 e ponto2 são pontos que representam as extremidades do seguimento de reta  
  
- [x] `Reta(ponto, vetorDiretor)`
ponto é um ponto pertencendo à reta  
vetorDiretor é o vetor diretor da reta paramétrica  
  
- [x] `Plano(ponto, vetorNormal)`
ponto é um ponto pertencendo ao plano  
vetorNormal é um vetor normal ao plano  
  
- [x] `Esfera(centro, raio)`
centro é um ponto que representa o centro da esfera  
raio é um valor real que representa o módulo do raio da esfera  
  
- [x] `Triangulo(ponto1, ponto2, ponto3)`
ponto1, ponto2 e ponto3 são pontos que representam os vértices do triângulo
  
- [x] `Base(v1, v2, v3)`
v1, v2, v3 são vetores que formam uma base (tendo de ser linearmente independentes)  

## FUNÇÕES

### Ferramentas básicas

- [x] `produtoEscalar(vetor1, vetor2) => n;`
vetor1 e vetor2 sendo dois vetores  
n sendo o valor do produto escalar entre vetor1 e vetor2  
  
- [x] `norma(vetor) => n;`
vetor é um vetor  
n é um número real que representa a norma desse vetor  
  
- [x] `normalize(vetor) => vetorNormalizado;`
vetor é um vetor  
vetorNomalizado é o vetor normalizado  
  
- [x] `cosseno(vetor1, vetor2) => angulo;`
vetor1 e vetor2 são vetores  
angulo é um número real que representa o ângulo em radianos  
  
- [x] `projecao(vetor1, vetor2) => vetor3;`
vetor1 e vetor2 são vetores  
vetor3 é o vetor-projeção do vetor1 no vetor2  
  
- [x] `produtoVetorial(vetor1, vetor2) => vetor3;`
vetor1 e vetor2 são vetores  
vetor3 é o vetor resultante do produto vetorial de vetor1 com vetor2  
  
- [x] `reflexao(vetor1, vetor2) => vetor3;`
vetor1 e vetor2 são vetores  
vetor3 é o vetor-reflexão do vetor1 em relação ao vetor3  
  
- [x] `saoParalelos(vetor1, vetor2) => boolean;`
vetor1 e vetor2 são vetores  
boolean é um valor booleano que afirma ou nega se o vetor1 é paralelo ao vetor2  
  
- [x] `saoOrtogonais(vetor1, vetor2) => boolean;`
vetor1 e vetor2 são vetores  
boolean é um valor booleano que afirma ou nega se vetor1 e vetor2 são ortogonais entre si  
  
- [x] `eLI([vetor1, ..., vetorn]) => boolean;`
[vetor1, vetor2, vetor3] é um array de três vetores
boolean é um valor booleano que afirma ou nega se vetor1, vetor2 e vetor3 são Linearmente Independentes

### Sobre objetos
- [x] `diretor(reta) => vetor;`
reta é uma reta
vetor é o vetor diretor da reta

- [x] `normal(plano) => vetor;`
plano é um plano
vetor é o vetor normal do plano

- [x] `eParalelo(vetor, reta) => boolean;`
vetor é um vetor
reta é uma reta
boolean é um valor booleano que afirma ou nega se o vetor é paralelo à reta

- [x] `eOrtogonal(vetor, plano) => boolean;`
vetor é um vetor
plano é um plano
boolean é um valor booleano que afirma ou nega se o vetor é ortogonal ao plano

- [x] `projecao(vetor, reta) => vetorProjetado;`
vetor é um vetor
reta é uma reta
vetorProjetado é o vetor projetado na reta

- [x] `projecao(vetor, plano) => vetorProjetado;`
vetor é um vetor
plano é um plano
vetorProjetado é o vetor projetado no plano

- [ ] `componenteOrtogonal(vetor, plano) => vetor;`
vetor é um vetor
plano é um plano
vetorOrtogonal é o componente ortogonal do vetor em relação ao plano

- [ ] `saoComplementosOrtogonais(reta, plano) => boolean;`
reta é uma reta
plano é um plano
boolean é um valor booleano que afirma ou nega que a reta seja complemento ortogonal do plano

- [ ] `saoComplementosOrtogonais(plano, reta) => boolean;`
plano é um plano
reta é uma reta
boolean é um valor booleano que afirma ou nega que o plano seja complemento ortogonal da reta

- [x] `formaCartesiana(plano) => [a,b,c,d]`
plano é um plano
[a,b,c,d] é um array com quatro números reais, onde a, ..., d são os coeficientes da equação que
define o plano na forma cartesiana, da seguinte maneira
ax + by + cz + d = 0

- [x] `formaCartesiana(reta) => [[a,b,c,d],[e,f,g,h]]`
[[a,b,c,d],[e,f,g,h]] é um array de dois arrays com quatro números reais, cada, onde a, ..., h são os
coeficientes das equações que definem a reta cartesiana, da seguinte maneira
ax + by + cz + d = 0
ex + fy + gz + h = 0

### Interseções
- [ ] `interseção(reta1, reta2) => objeto;`
reta1 e reta2 são retas
objeto é o ponto ou a reta correspondente à interseção da reta1 com a reta2 (se houver)

- [ ] `interseção(reta, plano) => objeto;`
reta é uma reta
plano é um plano
objeto é o ponto ou a reta correspondente à interseção da reta com o plano (se houver)

- [ ] `interseção(reta, esfera) => objeto;`
reta é uma reta
esfera é uma esfera
objeto é o ponto ou o par de pontos correspondentes à interseção da reta com a esfera (se houver)

- [ ] `interseção(reta, triangulo) => objeto;`
reta é uma reta
triangulo é um triangulo
objeto é o ponto ou o segmento correspondente à interseção da reta com o triangulo (se houver)

- [ ] `interseção(plano1, plano2) => objeto;`
plano1 e plano2 são planos
objeto é a reta ou o plano correspondente à interseção do plano1 com o plano2 (se houver)

### Base
- [x] `ortogonalize(base) => (baseOrtogonalizada);`
base é uma base
baseOrtogonalizada é uma base que sofreu o processo de Gram-schmidt na ordem da base

- [x] `mudeBase(vetor, base) => [x, y, z];`
vetor é um vetor
base é uma base
[x, y, z] é um array de três valores reais que representam as coordenadas do vetor na base

### Transformações Lineares
- [ ] `rotação(vetor, ângulo, sentido) => vetorRotacionado;`
vetor é um vetor
angulo é um valor real que representa o ângulo em radianos
sentido é uma das strings “H” ou “AH”, representando o sentido da rotação horário ou anti-horário
vetorRotacionado é o vetor resultante da rotação

- [ ] `rotação(vetor, ângulo, sentido, reta) => vetor;`
vetor é um vetor
angulo é um valor real que representa o ângulo em radianos
sentido é uma das strings “H” ou “AH”, representando o sentido da rotação horário ou anti-horário
reta é uma reta que representa o eixo de rotação arbitrário (o “sentido” da reta é dado pelo vetor
direto)
vetorRotacionado é o vetor resultante da rotação

- [ ] `reflexão(vetor, vetorNormal) => vetor;`
vetor é um vetor
vetorNormal é o vetor normal de um plano que passa pela origem
vetorRefletido é o vetor resultante da reflexão em relação ao plano

- [ ] `reflexão(vetor, vetorDiretor) => vetorRefletido;`
vetor é um vetor
vetorDiretor é o vetor diretor de uma reta que passa pela origem
vetorRefletido é o vetor resultante da reflexão em relação à reta

- [ ] `reflexão(vetor) => vetorRefletido;`
vetor é um vetor
vetorRefletido é o vetor resultante da reflexão em relação à origem

- [ ] `cisalhamento(vetor, eixos, fator) => vetorCisalhado;`
vetor é um vetor
eixos é uma das strings “XY”, “XZ”, “YX”, “YZ”, “ZX” ou “ZY” e representa o eixo que está sendo
cisalhado em relação ao eixo de referência do cisalhamento
fator é um valor real que representa o fator de cisalhamento
vetorCisalhado é o vetor resultante do cisalhamento

- [ ] `cisalhamento(vetor, eixos, fator1, fator2) => vetorCisalhado`,
vetor é um vetor
eixo é uma das strings “XYZ”, “YZX” ou “ZXY” e representa o eixo que está sendo cisalhado em
relação aos eixos de referência do duplo cisalhamento
fator1 é um valor real que representa o fator de cisalhamento do eixo subsequente
fator2 é um valor real que representa o fator de cisalhamento do outro eixo
vetorCisalhado é o vetor resultante do cisalhamento

- [ ] `deformação(vetor, fatorX, fatorY, fatorZ) => vetorDeformado;`
vetor é um vetor
fatorX é o fator de deformação do eixo X
fatorY é o fator de deformação do eixo Y
fatorZ é o fator de deformação do eixo Z

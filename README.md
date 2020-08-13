# sample_python
Três técnicas de amostragem utilizando python e cálculo simples de amostra

## Funções:
### calc_sample:
  Calcula a amostra conforme cálculo básico de amostra
   - n. = 1/(E.)²
   - n = (N*n.)/(N+n.)
   
  Onde:
  - n = tamanho da amostra
  - N = tamanho da população
  - E. = erro amostral tolerável
  - n. = primeira aproximação do tamanho da amostra
    
### simple_random_sample:
  Amostra simples, retorna elemento x, onde x é sua amostra.
  
### stratified_sample: 
 Consiste em olhar a população através de grupos;
 
 Cada individuo pode fazer parte de um unico grupo;
 
 Antes disso, precisamos importar o que é necessário para a amostra estratificada:
  - from sklearn.model_selection import train_test_split
  
### systematic_sample
  Geramos uma semente aleatoriamente e através dessa semente, os elementos são escolhidos sistematicamentes;
  Antes disso, precisamos importar a Numpy.

Esse exemplo foi fruto de um artigo do Minerando Dados: https://minerandodados.com.br/tres-tecnicas-de-amostragem-de-dados-utilizando-python/

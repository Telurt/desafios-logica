
'''
Escreva um programa que receba a entrada de inteiros N e M, seguidos por N mais inteiros e depois M mais inteiros. Para cada um dos últimos M números, o programa gera verdadeiro; se esse número estiver presente na matriz de N números, gera False, caso contrário.

Suas linhas de saída não devem ter nenhum espaço em branco à direita ou à esquerda
Implementado preferencialmente em PYTHON 3
Restrições:
0 <N <20.000

0 <M <15.000

Entrada
4 2
99 12 10 23
23
25

Resultado
Verdadeiro
Falso

Explicação: Uma entrada de tamanho 4 é aceita, seguida por 2 linhas. 23 gera True, já que 23 está presente na matriz acima, 25 gera falso porque não estava na matriz de N inteiros.
'''
import sys

# complete the linear_search function below
def linear_search(n, m):

  for valor in m:
    if valor in n:
      print('True')
    else:
      print('False')  

nm = input().split()
n_size, m_size = int(nm[0]), int(nm[1])
n = list(map(int, input().rstrip().split()))
m = []
for i in range(m_size):
    m.append(int(input()))
linear_search(n, m)
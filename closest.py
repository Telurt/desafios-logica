'''

Escreva um programa que recebe a entrada de um inteiro N, seguido por N inteiros. O programa então produz o número mais próximo da média desses N inteiros. Se houver mais de uma solução, imprima aquela que vier primeiro na lista de entrada.

Suas linhas de saída não devem ter nenhum espaço em branco à direita ou à esquerda
Em caso de erro, sua saída deve ser 0
Implementado preferencialmente em PYTHON 3
Entrada
5
1 2 3 4 6

Resultado
3
Explicação: A média é 3,2 para {1,2,3,4,6}. Portanto, 3 é o mais próximo
'''


import sys
# complete the closest_to_average function below

def closest(x,arr):
  valor = max(arr)
  ind = 0
  
  for i in range(len(arr)):
    if (abs(x-arr[i]) < valor):
      valor = abs(x-arr[i])
      ind = i 
  return arr[ind]

def closest_to_average(n, arr):
  media = (sum(arr)/n)
  return closest(media,arr)
  
n = int(input())
arr = list(map(int, input().rstrip().split()))
print(closest_to_average(n, arr))
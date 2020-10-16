'''
Dados 3 números, inteiros positivos, A, B e X, escreva um programa que imprima os números de 1 a X. Mas para os múltiplos de A imprima "A" em vez do número e para os múltiplos de B imprima "B". Para números que são múltiplos de A e B, imprima "AB".

A primeira linha contém o número de casos de teste
Cada linha contém 3 números delimitados por espaço
Cada linha de entrada deve ter uma linha de saída
Suas linhas de saída não devem ter nenhum espaço em branco à direita ou à esquerda
Em caso de erros, sua saída deve ser 0
Implementado preferencialmente em PYTHON 3
Por exemplo:

Entrada:
1
2 7 14

Resultado:
1 A 3 A 5 A B A 9 ​​A 11 A 13 AB
'''
import sys

# Complete the multiples function below
def multiples(a, b, x):

  lista = list(range(1, x+1))
  for i in range(len(lista)): 
    if(lista[i] %a==0 and lista[i] %b==0): 
      lista[i] = 'AB'
    elif(lista[i] %a==0): 
      lista[i] = 'A'
    elif(lista[i] %b==0):
      lista[i] = 'B'
    else: 
      lista[i] = str(lista[i])
  return ' '.join(lista)
    
n = int(input())
for i in range(n):
    arr = list(map(int, input().rstrip().split()))
    print(multiples(arr[0], arr[1], arr[2]))
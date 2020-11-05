'''

Escreva um programa que receba a entrada do inteiro N, seguido por mais N inteiros. Para cada número inteiro. Produza o próximo número de Fibonacci após ele.

Número de Fibonacci: qualquer número que pertença à série de fibonacci.

A série de Fibonacci é definida como: F (0) = 0; F (1) = 1; F (n) = F (n – 1) + F (n – 2) quando n> 1

Suas linhas de saída não devem ter nenhum espaço em branco à direita ou à esquerda
Em caso de erro, sua saída deve ser 0
Implementado preferencialmente em PYTHON 3
Restrições:

Seu programa deve ser executado corretamente para os primeiros 60 números de Fibonacci
Entrada
3
1
9
22

Resultado
2
13
34
Explicação: 2 é o próximo número de fibonacci maior que 1, o número de fibonacci que vem depois de 9 é 13. 34 é o próximo número de fibonacci após 22
'''

import sys

# complete the next_fibonacci function below


def next_fibonacci(n):
  fibo = [0,1]
  while (fibo[-1] < n):
    fibo.append(fibo[-2]+fibo[-1])
  return fibo[-1]
  
n = int(input())
for _ in range(n):
    f = int(input())
    print(next_fibonacci(f))

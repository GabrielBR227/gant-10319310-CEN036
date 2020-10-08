#!/usr/bin/env python3

import sys #importação do sys

  # função paa colocar os argumentos

try:
        a = int(sys.argv[1])
except ValueError:
        print("a não é um número inteiro, insira novamente")

try:
        b  = int(sys.argv[2])
except ValueError:
        print('b não é um número inteiro, insira novamente')

print(isinstance(a and b, int))      #Verifica se a e b são inteiros


if ((a<=0 or a>1000) and (b<=0 or b>1000)):       #verifica se a e b estão entre 0 e 1000, e depois printa na tela o quadrado da hipotenusa
        print('erro argv 1 e erro argv 2: insira o primeiro e segundo número novamente: maior que 0 e menor que 1000')

elif (a<=0 or a>1000):       #verifica se a está entre 0 e 1000 e mostra mensagem de erro se não estiver
        print('erro argv 1: insira o primeiro número novamente: maior que 0 e menor que 1000')

elif (b<=0 or b>1000):     #verifica se b está entre 0 e 1000 e mostra mensagem de erro se nao estiver
        print('erro argv 2: insira o segundo número novamente: maior que 0 e menor que 1000')

else:               #verifica se a e b estão entre 0 e 1000, e depois printa na tela o quadrado da hipotenusa
        print("O quadrado da hipotenusa para o triângulo retângulo com lados a = {} e b = {}, é {}.".format(a,b,round(((a**2+b**2)**0.5),2)))

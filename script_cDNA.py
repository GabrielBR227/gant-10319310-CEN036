#!/usr/bin/env python3

import sys  #aqui foi importado sys
 
DNA = str(sys.argv[1])   #input da variável DNA, com dna1 sendo a versão "normalizada" pela função upper()
DNA1 = DNA.upper()

n1 = int(sys.argv[2])   #input das variáveis n1 n2 n3 n4

n2 = int(sys.argv[3])

n3 = int(sys.argv[4])

n4 = int(sys.argv[5])

if isinstance(DNA1, str) == False:   #Confirmação do tipo das variáveis e as mensagens de erro
	print("Digite uma STRING")


if isinstance(n1 and n2 and n3 and n4, int) == False:
	print("Digite números inteiros")   

	
print("PARA O CÓDIGO FUNCIONAR: Escreva os números em ordem crescente e que sejam menores que DNA")

if n1<n2<n3<n4<len(DNA1):                               #função if para atender o requiisito das variáveis n não serem maiores que a fita de DNA e estarem em ordem crescente. Se não atenderem será mostrada uma mensagem de erro 
	print("Você digitou uma sequência correta")
else:
	print("***ERRO***: ESCREVA OS NÚMERS EM ORDEM CRESCENTE E QUE SEJAM MENORES QUE DNA!")
	

if DNA1[n1-1:n1+2] != "ATG":         #Para verificar se CDS1 não começa com as letras ATG
	print("CDS1 não inicia com códon de início")

if DNA1[n4-1:n4+2] == "TAA":          #no if e elif verifica-se se CDS2 termina com os nucleotídeos corretos. Em caso negativo, o else mostra a mensagem de erro
	print(DNA1[n1-1:n2-1]+DNA1[n3-1:n4-1])
elif DNA1[n4-1:n4+2] == "TGA":
	print(DNA1[n1-1:n2-1]+DNA1[n3-1:n4-1])
elif DNA1[n4-1:n4+2] == "TAG":
	print(DNA1[n1-1:n2-1]+DNA1[n3-1:n4-1])
else: 
	print("CDS2 não termina com códon de parada")


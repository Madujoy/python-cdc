'''Python'''
# Arrays (vetores/matrizes utiliando a biblioteca NumPy)
import numpy as np 

#Criando um array NumPy unidimencional a partir de uma lista
array = np.array([1, 2, 3, 4, 5])
print("Array:", array)

#Acessando elementos do array:
# - Indices começam em 0
# - Indices negativos acessam a partir do final
print("Primeiro elemento:", array[0])
print("Ultimo elemento:", array[-1])

# SLicing (fatiamento) de arrays:
# - Sintaxe: [inicio:fim]
# - O indice final nao e incluido
print("Elementos do indice 1 a 3 (exclusivo):", array[1:3])

#Listas (estrutura mutavel de elementos)
#Criando uma lista basica
my_list = [1, 2, 3, 4, 5]
print("Lista original:", my_list)

#Adicionando um elemento ao final da lista
my_list.append(6)
print("Lista apos adicionar 6:", my_list)

#Inserindo um elemento em posiçao especifica:
# - Sintaxe: insert(indice, valor)
# - Desloca elementos existentes para a direita
my_list.insert(2, 7)
print("Lista apos inserir 7 na posiçao 2:", my_list)

# Removendo a primeira ocorrencia de um elemento
print("Ultimo elemento:", array[-1])

my_list.remove(4)
print("Lista apos remover o valor 4:", my_list)

# Tuplas (estrutura imutavel e elementos)
# Criando uma tupla - usa parenteses o inves de colchetes
my_tuple = (1, 2, 3, 4, 5)
print("Tupla:", my_tuple)

# Acesso elementos funciona igual as listas
print("Primeiro elemento da tupla:", my_tuple[0])
print("Ultimo elemento da tupla:", my_tuple[-1])

# Loops (estruturas de repetiçao)

# Loop for iterando sobre elementos de uma lista
fruits = ["maça", "banana", "morango"]
print("Frutas na lista:")
for fruit in fruits:
    print(fruit)

# Loop while executando enquanto condiçao e verdadeira
print("Contagem de 0 a 4:")
i = 0
while i < 5:
    print(i)
    i += # Incrementa o contador

# Loop for com acesso ao indice e elemento simultaneamente usando enumerate
print("Elementos da lista com seus indices:")
my_list = [1, 2, 3, 4, 5]
for indice, elemento in enumerate(my_list):
    print(f"Indice {indice}: {elemento}")
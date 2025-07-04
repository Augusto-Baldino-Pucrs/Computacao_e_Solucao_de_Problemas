# Funções lambda (anônimas)
# Sintaxe:
# lambda argumentos: expressão

# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))

# par= lambda x: x %2 == 0
# print(par(9))

# f_c = lambda f: (f-32) * 5/9
# print(f_c(32))

# Função Map()
#Sintaxe
# map(função, iteravel)

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# palavras = ['Python', 'é', 'uma', 'linguagem', 'de','programação']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

# Função filter()
#Sintaxe:
#filter(função,sequência)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numeros_pares = list(filter(lambda x: x % 2 == 0, snumeros))

# print(f"Números pares: {numeros_pares}")

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num_impar = list(filter(lambda x: x % 2 != 0, numeros))

# print(num_impar)

# Função reduce()
# Sintaxe
# reduce(função,seqûencia, valor_inicial)

from functools import reduce

# def mult(x,y):
#     return x * y

# numeros = [1,2,3,4,5,6]

# total= reduce(mult, numeros)
# print(total)

# Somacumulativa dos quadrados dos valores , usando expressão lambda

numeros = [1,2,3,4]

total= reduce(lambda x, y: x**2 + y**2,numeros)
print(total)
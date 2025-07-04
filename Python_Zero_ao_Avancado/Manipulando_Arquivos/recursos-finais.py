#Trocar valores entre duas variáveis

var1 = 122
var2 = 31

# var2, var1 = var1, var2

# print(f'var1: {var1} var2: {var2}')

# Operador Condicional ternário

# menor = var1 if var1<var2 else var2
# print(f'Menor valor: {menor}')
# print(f'Menor valor: {(var1,var2) [var1 < var2s]}')

# Generators consome menos recursos na memória

# valores = [1,3,5,7,9,11,13,15]
# quadrados = (item **2 for item in valores)
# print(quadrados)
# for valor in quadrados:
#     print(valor)

# Função enumerate()

# bebidas = ['Café','Chá','Água','Suco', 'Refrigerante']
# for i, item in enumerate(bebidas):
#     print(f'Ìndice: {i}, Item: {item}')

# temperaturas =  [-1,10,5,-3,8,4,-2,-5,7]
# total = 0

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         print(f'A temperatura {i} é negativa, com {t} Celsius')

#Gerenciamentode contexto  com with

try:
    a= open('6 Semestre/Computacao-Solucao-Problemas/Python_Zero_ao_Avancado/Manipulando_Arquivos/frutas.txt', 'r', encoding='utf-8')
    print(a.read())
except IOError:
    print('Não foi possível avriro arquivo')
else:
    a.close

with open('6 Semestre/Computacao-Solucao-Problemas/Python_Zero_ao_Avancado/Manipulando_Arquivos/frutas.txt', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha)






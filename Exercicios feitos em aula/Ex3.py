# Faça um programa em Python que lêtrês números inteiros do teclado. Após, o programa
# deve apresentar na tela quantos dos valores digitados foram pares. Além disso, o programa
# deve imprimir na tela qual dos três valores é o maior.

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))


n_pares = 0
if(n1%2 == 0):
    n_pares += 1
if(n2%2 ==0 ):
    n_pares += 1
if(n3%2 ==0 ):
    n_pares += 1

print(f"Dos números que você digitou: {n_pares} são pares")

if(n1>n2 and n1>n3):
    print(f"O maior número é: {n1}")
elif(n2> n1 and n2>n3):
    print(f'O maior número é: {n2}')
else:
    print(f'O maior número é: {n3}')
    
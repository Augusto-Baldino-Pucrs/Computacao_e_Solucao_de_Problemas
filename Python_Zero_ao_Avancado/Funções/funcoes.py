# def mensagem():
#     print('Gutebas')
#     print('Pigas')
    
# mensagem()

#Funcao com argumentos

# def soma(a,b):
#     print(a+b)

# soma(12,7)

# def multi(x,y):
#     return x*y

# a = 5
# b = 8
# c = multi(a,b)
# print(f'Produto de {a} e {b} é {c}')

# def div(k, j):
#     return k / j

# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite um número: '))
    
#     # Verificação para evitar divisão por zero
#     if b == 0:
#         print("Erro: Divisão por zero não é permitida.")
#     else:
#         r = div(a, b)
#         print(f'{a} dividido por {b} é igual a {r}')

# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados

# def contar(num=11, caractere='+'):
#     for i in range(1,num):
#         print(caractere)

# if __name__ == '__main__':
#     contar(caractere='&')

x = 5
y = 6
z = 3

def soma_mult(a,b,c = 0):
    if c==0:
        return a*b
    else:
        return a + b + c
if __name__ == '__main__':
    res = soma_mult(x,y,z  )
    print(res)
    
        


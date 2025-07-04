import random

# print('Gerar 5 números aleatórios entre 1 e 50')
# for i in range(5):
#     n= random.randint(1,50)
#     print(f'número gerado: {n}')

# valor = random.random()
# print(f'Número gerado: {round(valor *10,2)}')

# valor = random.uniform(1,100)
# print(f'número: {round(valor,4)}')

L = [2,4,6,9,10,13,14,20,26,1]
# n = random.choice(L)
# print(f'Número escolhido: {n}')

# n = random.sample(L,3)
# print(f'Números escolhidos: {n}')

#Embaralhar
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibilá:')
n = random.shuffle(L)
print(L)


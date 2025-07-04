from random import randint
#Ignora o primeiro index da lista, pois as listas começam a contar em 0
dados = ['''
|---|
| 0 |
|---|
''',
    '''
|-------|
|       |
|   o   |
|       |
|-------|
''',
    '''
|-------|
| o     |
|       |
|     o |
|-------|
''',
    '''
|-------|
| o     |
|   o   |
|     o |
|-------|
''',
    '''
|-------|
| o   o |
|       |
| o   o |
|-------|
''',
    '''
|-------|
| o   o |
|   o   |
| o   o |
|-------|
''',
    '''
|-------|
|  o o  |
|  o o  |
|  o o  |
|-------|
'''
]

print('Os dados foram lançados')
for _ in range (5):
    n = randint(1,6)
    dados.append(n)
    print(f'{dados[n]} {n}')
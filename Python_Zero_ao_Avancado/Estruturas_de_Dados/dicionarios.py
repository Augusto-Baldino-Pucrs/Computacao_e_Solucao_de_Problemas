# Dicionarios ou Hashes
#Imutáveis

elemento = {
    'Z': 3,
    'nome': 'Litio',
    'grupo': 'Metais alcalinos',
    'densidade': 0.534
}

# print(f"Elemento: {elemento['nome']}")
# print(f"Elemento: {elemento['densidade']}")
# print(f'O dicionário possui {len(elemento)} elementos')

#Atualizar entrada
elemento['grupo'] = 'Alcalinos'
#print(elemento)

#Adicionando uma entrada
elemento['periodo'] = 1
#print(elemento)

#Exclusão de itens em dicionários
# del elemento['periodo']
# print(elemento)

# elemento.clear()
# print(elemento)

# del elemento
# print(elemento)

# print(elemento.items())
# for i in elemento.items():
#     print(i)
    
# print(elemento.keys())
# for i in elemento.keys():
#     print(i)
    
# print(elemento.values())
# for i in elemento.values():
#     print(i)


for i, j in elemento.itens():
    print(f'{i}:{j}')



# São imutáveis, o conteudo de uma tupla não pode ser modificado

# tupla = (2,4,6,7,9)
# tupla[1] = 5
# print(tupla)

halogenios = ('F', 'Cl','Br','I','At')
gasesNobres = ('He','Ne','Ar','Xe','Kr','Rn')
elementos = halogenios + gasesNobres
# print('Cl' in halogenios)

#Operações não disponiveis em tuplas: .sort(), append(), reverse(), pop()

# for elemento in elementos:
#     print("Elementos químicos:" + elemento)

# grupo17 = list(halogenios)
# grupo17[0] = 'H'
# print(grupo17)

grupo1 = ['Li','Na','K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)

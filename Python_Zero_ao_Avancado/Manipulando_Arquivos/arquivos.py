#Manipulação de arquivos de texto.


# print(f'\Método read():\n')
# print(manipulador.read())

# print(f'\Método readline():\n')
# print(manipulador.readline())

# print(f'\Método readlines():\n')
# print(manipulador.readlines())

# texto = input('Qual o termo que deseja porcurar no arquivo?')
# try:

#     manipulador = open('6 Semestre/Computacao-Solucao-Problemas/Python_Zero_ao_Avancado/Manipulando_Arquivos/arquivo.txt', 'r', encoding='utf-8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#             print(f'A string foi encontrada')
#             print(linha)
#         print(linha)
#     else:
#         print(f'String não encontrada')

# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador.close()

# Escrever em arquivos de texto 8:27:00

# try:
#     manipulador = open('6 Semestre/Computacao-Solucao-Problemas/Python_Zero_ao_Avancado/Manipulando_Arquivos/arquivo.txt', 'a', encoding='utf-8')
#     manipulador.write('Pythn é muito usado em IA\n')
#     manipulador.write('Inteligência artificial veio para ficar')
# except IOError:
#      print(f'Não foi possível abrir o arquivo')
# else:
#      manipulador.close()

frutas = ['Morango\n', 'Uva\n', 'Caju\n','Amora\n', 'Framboesa\n','Graviola']
try:
    manipulador = open('6 Semestre/Computacao-Solucao-Problemas/Python_Zero_ao_Avancado/Manipulando_Arquivos/frutas.txt', 'a', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
     print(f'Não foi possível abrir o arquivo')
else:
     manipulador.close()
     
#Ler o arquvi criado
try:
     manipulador = open('6 Semestre/Computacao-Solucao-Problemas/Python_Zero_ao_Avancado/Manipulando_Arquivos/frutas.txt', 'a', encoding='utf-8')
     print(manipulador.read())
except IOError:
     print(f'Não foi possível abrir o arquivo')
else:
     manipulador.close()
#Desenvolva um pograma em python p/ calcular as perdas em um diodo
import math

print('Calcule as perdas do Diodo')
print('Digite a resistencia do Diodo')
resitenciaDiodo = input()
print('Digite a corrente eficaz')
correnteEficaz = input()
print('Digite a tensão sobre o diodo ')
tensaoSobreDiodo = input()
print('Digite a corrente média')
correnteMedia = input()

perdaMedia = int(resitenciaDiodo) * (math.pow(int(correnteEficaz),2)) + int(tensaoSobreDiodo) * int(correnteMedia)
print(f'A perda média é {perdaMedia}')


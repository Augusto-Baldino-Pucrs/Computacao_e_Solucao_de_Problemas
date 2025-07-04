print('Bora calcular a média do semestre pra vermos se você passou')
print('Digite a nota 1')
n1 = float(input())
print('Digite a nota 2')
n2 = float(input())
print('Digite a nota 3')
n3 = float(input())

G1 = (n1+n2+n3)/3

if(G1>=7):
    print(f'A sua média é: {G1}')
    print('Parabéns, vocẽ foi aprovado')
    NF=G1
else:
    print('Sua nota foi abaixo da média. Terá que fazer recuperação')
    print('Digite aqui a nota final do exame')
    G2 = float(input())
    NF = (G1 + G2) / 2
    print(f'Sua nota final foi: {NF}')
    if(NF < 5):
        print(f'Infelizmente você foi reprovado')
    else:
        print('Parabéns, vocẽ foi aprovado')
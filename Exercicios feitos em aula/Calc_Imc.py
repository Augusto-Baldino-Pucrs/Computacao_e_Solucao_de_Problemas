

print("Vamos calcular o seu IMC, primeiro diga a sua altura em metros(Seja honesto)")
altura = float(input())
print("Digite o seu peso em kilos")
peso = float(input())

imc = peso / (altura * altura)

# if(imc< 18.5):
#     print(f'Seu imc é {imc}, você está com baixo peso')
# if(imc > 18.5 and imc <=24.99):
#     print(f'Seu imc é {imc}, você está com o peso normal')
# if(imc >= 25 and imc <=29.99):
#     print(f'Seu imc é {imc}, você está com sobrepeso')
# else:
#     print(f'Seu imc é {imc}, você está obeso')
if imc < 18.5:
    print(f'Seu imc é {imc}, você está com o peso Abaixo do peso')
elif 18.5 <= imc < 24.9:
        print(f'Seu imc é {imc}, você está com o Peso normal')
elif 24.9 <= imc < 29.9:
    print(f'Seu imc é {imc}, você está com sobrepeso')
elif 29.9 <= imc < 34.9:
    print(f'Seu imc é {imc}, você está com Obesidade grau I')
elif 34.9 <= imc < 39.9:
    print(f'Seu imc é {imc}, você está com Obesidade grau II')
else:
    print(f'Seu imc é {imc}, você está com Obesidade grau III')
    

    
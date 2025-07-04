import math

print('Vamos calcular a média aritmética simples e o desvião padrão')
print('Diga a primeira medida')
x = float(input()) 
print('Diga a segunda medida')
y = float(input()) 
print('Diga terceira medida')
z = float(input()) 
media = (x + y + z) / 3

desvioPadrao = math.sqrt(((math.pow(x-media,2))+ (math.pow(y-media,2))+ (math.pow(z-media,2)))/3)
print(f'A média aritmética das 3 variáveis é {media}')
print(f'O desvião padrão das 3 variáveis é {desvioPadrao}')

#Exceção é um obejeto que representa um erro que ocorreu ao executur o programa
#Blocos try ... except

def div(k,j):
    return round(k/j,2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número:'))
            n2 = int(input('Digite outro número:'))
            break
        except ValueError:
            print(f'Ocorreu um erro ao ler o valor. Tente novamente')
        
    try:
        r = div(n1,n2)
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    except:
        print('Erro desconhecido')
    else:
        print(f'Resultado: {r}')
    finally:
        print(f'\nFim do cálculo')


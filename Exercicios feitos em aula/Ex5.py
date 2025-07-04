from math import factorial

def calculo_pi(n):
    soma = 0
    for i in range(n+1):
        resultado = ((-1)**i) / (2*i + 1)
        soma += resultado
        
    return  4 * soma

def calculo_euler(n):
    soma = 0
    for i in range(n+1):
      resultado =  1/(factorial(i))
      soma+= resultado
    
    return soma

if __name__ == '__main__':
    comando = True
    while comando:

        opcao = input("\033[93mDigite a opção desejada (1/2/3): 1 para calcular pi, 2 para calcular euler e 3 para sair \033[0m")
        
        if opcao == '3':
            print("\033[91mSaindo...\033[0m")
            comando = False
            break
        
        if opcao not in ['1', '2']:
            print("\033[91mOpção inválida! Tente novamente.\033[0m")
            continue
        
        n = int(input("\033[94mDigite o número de iterações: \033[0m"))
        
        if opcao == '1':
            res = calculo_pi(n)
            print(f"\033[92mAproximação de π com {n} iterações: {res}\033[0m")
        
        if opcao == '2':
            res = calculo_euler(n)
            print(f"\033[92mAproximação de euler com {n} iterações: {res}\033[0m")
        
        print("\n" + "=" * 40 + "\n")
    
        
        

        
    
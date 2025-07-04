import requests
import matplotlib.pyplot as plt

def contaAcertos(sorteio, aposta):
    sorteio_set = set(sorteio)  # Converte para conjunto para otimizar a busca
    num_ac = [num for num in aposta if num in sorteio_set]  # Compreensão de lista para encontrar acertos
    return len(num_ac), num_ac

def mostrar_grafico(qtd_acertos):
    indices = list(range(len(qtd_acertos)))
    plt.bar(indices, qtd_acertos)
    plt.title('Quantidade de Acertos por Sorteio')
    plt.xlabel('Índice do Sorteio')
    plt.ylabel('Número de Acertos')
    plt.xticks(indices)  # Para mostrar os índices no eixo x
    plt.show()

def main():
    while True:
        print("\nMenu:")
        print("1. Fazer uma nova aposta")
        print("2. Visualizar resultados")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Lista de números apostados
            leitura = input('Digite os números desejados (separados por vírgula): ')
            num_apost = leitura.split(',')

            # Quantidade de sorteios a analisar
            qtd_sorteios = int(input('Quantos sorteios queres analisar? '))
            qtd_acertos = []

            # URL base para a API
            base_url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena'

            # Solicita o sorteio mais recente
            resp = requests.get(base_url)
            sorteio = resp.json()

            # Processa o sorteio mais recente
            acertos, num_ace = contaAcertos(sorteio['listaDezenas'], num_apost)
            qtd_acertos.append(acertos)
            print(f'Acertos no sorteio mais recente: {acertos}')

            # Pega o número do concurso anterior para os próximos sorteios
            nca = sorteio['numeroConcursoAnterior']

            # Itera para os sorteios anteriores
            for _ in range(qtd_sorteios - 1):    
                resp = requests.get(f"{base_url}/{nca}")  # Requisição direta usando a URL concatenada
                sorteio = resp.json()
                
                acertos, num_ace = contaAcertos(sorteio['listaDezenas'], num_apost)
                qtd_acertos.append(acertos)
                print(f'Acertos no sorteio {nca}: {acertos}')

                # Atualiza o número do concurso anterior
                nca = sorteio['numeroConcursoAnterior']

            # Exibe a lista completa de acertos ao final
            print("Quantidade de acertos por sorteio:", qtd_acertos)

        elif opcao == '2':
            # Se não houver dados, avisa o usuário
            if 'qtd_acertos' not in locals() or not qtd_acertos:
                print("Nenhuma aposta foi feita ainda.")
            else:
                mostrar_grafico(qtd_acertos)

        elif opcao == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

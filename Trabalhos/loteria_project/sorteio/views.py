from django.shortcuts import render
import requests
from .models import Aposta, ResultadoSorteio
from django.http import JsonResponse
import matplotlib.pyplot as plt
import io
import base64
import time

def index(request):
    if request.method == 'POST':
        start_time = time.time()

        numeros_apostados = request.POST.get('numeros').split(',')
        tipo_loteria = request.POST.get('tipo_loteria')
        qtd_sorteios = int(request.POST.get('qtd_sorteios'))
        qtd_acertos = []
        sorteios_premiados = []

        base_urls = {
            'megasena': 'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena',
            'lotofacil': 'https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil',
            'quina': 'https://servicebus2.caixa.gov.br/portaldeloterias/api/quina',
        }
        base_url = base_urls.get(tipo_loteria, base_urls['megasena'])

        # Consultar o último sorteio
        resp = requests.get(base_url)
        sorteio = resp.json()
        acertos, num_ac = conta_acertos(sorteio['listaDezenas'], numeros_apostados)
        qtd_acertos.append(acertos)
        verifica_premiacao(tipo_loteria, acertos, sorteios_premiados, sorteio['numero'])

        aposta = Aposta.objects.create(numeros=",".join(numeros_apostados), tipo=tipo_loteria)
        ResultadoSorteio.objects.create(
            numero_concurso=sorteio['numero'],
            dezenas=",".join(sorteio['listaDezenas']),
            acertos=acertos,
            aposta=aposta
        )

        nca = sorteio['numeroConcursoAnterior']
        for _ in range(qtd_sorteios - 1):
            resp = requests.get(f"{base_url}/{nca}")
            sorteio = resp.json()
            acertos, num_ac = conta_acertos(sorteio['listaDezenas'], numeros_apostados)
            qtd_acertos.append(acertos)
            verifica_premiacao(tipo_loteria, acertos, sorteios_premiados, sorteio['numero'])
            nca = sorteio['numeroConcursoAnterior']

            ResultadoSorteio.objects.create(
                numero_concurso=sorteio['numero'],
                dezenas=",".join(sorteio['listaDezenas']),
                acertos=acertos,
                aposta=aposta
            )

        plt.figure(figsize=(10, 5))
        plt.plot(range(1, qtd_sorteios + 1), qtd_acertos, marker='o')
        plt.title('Acertos por Sorteio')
        plt.xlabel('Sorteio Avaliado')
        plt.ylabel('Número de Acertos')
        plt.grid()
        graph1 = save_graph_to_base64()

        plt.figure(figsize=(10, 5))
        todas_dezenas = [int(num) for sorteio in ResultadoSorteio.objects.filter(aposta=aposta)
                         for num in sorteio.dezenas.split(',')]
        bins = range(1, 62)  
        frequencias, _, _ = plt.hist(todas_dezenas, bins=bins, color='blue', alpha=0.7, rwidth=0.85)

        for i, freq in enumerate(frequencias, start=1):
            if freq == 0:
                plt.bar(i, 0, color='blue', alpha=0.7, edgecolor='black', linewidth=0.5)

        plt.title('Frequência das Dezenas')
        plt.xlabel('Dezena')
        plt.ylabel('Frequência')
        plt.grid(axis='y')
        graph2 = save_graph_to_base64()

        end_time = time.time()
        execution_time = end_time - start_time

        return render(request, 'sorteio/resultados.html', {
            'qtd_acertos': qtd_acertos,
            'sorteios_premiados': sorteios_premiados,
            'graph1': graph1,
            'graph2': graph2,
            'execution_time': f"{execution_time:.2f} segundos"
        })

    return render(request, 'sorteio/index.html')


def verifica_premiacao(tipo_loteria, acertos, sorteios_premiados, numero_concurso):
    premiacoes_minimas = {'megasena': 4, 'lotofacil': 11, 'quina': 2}
    if acertos >= premiacoes_minimas[tipo_loteria]:
        sorteios_premiados.append(f"$$ Prêmio!! $$ Sorteio:{numero_concurso} {acertos} Acertos! Verifique com sua casa de apostas!")

def conta_acertos(sorteio, aposta):
    sorteio_set = set(sorteio)
    num_ac = [num for num in aposta if num in sorteio_set]
    return len(num_ac), num_ac

def save_graph_to_base64():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')

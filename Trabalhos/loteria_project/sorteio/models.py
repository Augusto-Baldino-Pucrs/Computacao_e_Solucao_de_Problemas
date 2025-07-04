from django.db import models

class Aposta(models.Model):
    numeros = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, default='megasena')

    def __str__(self):
        return f"{self.tipo}: {self.numeros}"


class ResultadoSorteio(models.Model):
    numero_concurso = models.IntegerField()
    dezenas = models.CharField(max_length=50)
    acertos = models.IntegerField()
    aposta = models.ForeignKey(Aposta, on_delete=models.CASCADE)

    def __str__(self):
        return f"Concurso {self.numero_concurso}: {self.acertos} acertos"


class FrequenciaDezena(models.Model):
    dezena = models.IntegerField()
    frequencia = models.IntegerField()

    def __str__(self):
        return f"Dezena {self.dezena}: {self.frequencia} ocorrências"

from django.db import models
from django.forms import ModelForm

# Create your models here.
class Aluno(models.Model):
    nome = models.TextField()


    def __str__(self):
        return self.nome


class Experimento_Pratico(models.Model):
    experimento_p = models.IntegerField(primary_key=True)
    temp_ebulicao_p = models.FloatField()
    concentracao_p = models.FloatField(default=None)
    categoria = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.experimento_p



class Criacao_Aluno(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome']



class CriacaoExperimento:
    class Meta:
        model = Experimento_Pratico
        fields = ['temp_ebulicao_p', 'concentracao_p', 'categoria']
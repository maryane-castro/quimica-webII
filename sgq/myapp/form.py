from django.forms import ModelForm
from .models import Experimento_Teorico

class ExpT_Form(ModelForm):
    class Meta:
        model = Experimento_Teorico
        fields = ['temp_ebulicao_t', 'concentracao_t']

        
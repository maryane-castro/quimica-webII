from django.contrib import admin

# Register your models here.

from .models import Aluno
from .models import Experimento_Pratico
from .models import Experimento_Teorico


admin.site.register(Aluno)
admin.site.register(Experimento_Pratico)
admin.site.register(Experimento_Teorico)
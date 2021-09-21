from django.forms import ModelForm
from app.models import Segmentos

class Segmentos_form(ModelForm):
    class Meta:
        model : Segmentos
        fiels = ['segmento', 'descricao_segmento']
from django.forms import ModelForm
from app.models import Empresas

class SegmentosForm(ModelForm):
    class Meta:
        model = Empresas
        fields = ['segmentos', 'marcas', 'produtos']


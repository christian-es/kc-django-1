from blog.models import Articulo
from django.forms import ModelForm


class ArticuloForm(ModelForm):

    class Meta:
        model = Articulo
        exclude = ['created_by']
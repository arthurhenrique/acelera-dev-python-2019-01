from django.shortcuts import render
from .models import Autor
from django.views.generic import TemplateView
from django.views.generic import ListView
# Create your views here.

def index(request):
    context = {
            'lang': 'Python',
            'autores': Autor.objects.all(),
            }
    return render(request, 'index.html', context)

class IndexView(TemplateView):
    template_name =  'templates.html'

class AutorView(ListView):
    models = Autor
    template_name = 'index.html'
    context_object_name = 'autores'

    def get_queryset(self):
        return self.models.objects.all()

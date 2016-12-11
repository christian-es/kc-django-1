from blog.models import Articulo
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(View):
    def get(self, request):
        return render(request, 'blog/home.html')


class BlogView(View):
    def get(self, request):
        articulos = Articulo.objects.all()
        context = {'articulos_list': articulos}
        return render(request, 'blog/articulos.html', context)
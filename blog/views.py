from blog.models import Articulo
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(View):
    def get(self, request):
        return render(request, 'blog/home.html')


class BlogsView(View):
    def get(self, request):
        usuarios = User.objects.all()
        context = {'usuarios_list': usuarios}
        return render(request, 'blog/blogs.html', context)


class PostView(View):
    def get(self, request, username):
        usuario = User.objects.filter(username=username)
        posts = Articulo.objects.filter(created_by_id=usuario[0].pk)
        context = {'post_list': posts}
        return render(request, 'blog/post.html', context)
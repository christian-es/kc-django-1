from blog.forms import ArticuloForm
from blog.models import Articulo
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(View):
    def get(self, request):
        posts = Articulo.objects.all().order_by('-created_at')
        context = {'post_list': posts}
        return render(request, 'blog/home.html', context)


class BlogsView(View):
    def get(self, request):
        usuarios = User.objects.all()
        context = {'usuarios_list': usuarios}
        return render(request, 'blog/blogs.html', context)


class PostListView(View):
    def get(self, request, username):
        usuario = User.objects.filter(username=username)
        posts = Articulo.objects.filter(created_by_id=usuario[0].pk).order_by('-created_at')
        context = {'post_list': posts}
        return render(request, 'blog/post.html', context)


class PostDetailView(View):
    def get(self, request, username, pk):
        possible_usuario = User.objects.filter(username=username)

        if len(possible_usuario) == 0:
            return HttpResponseNotFound("El usuario no existe")
        elif len(possible_usuario) > 1:
            return HttpResponse("Múltiples opciones", status=300)

        post = Articulo.objects.filter(pk=pk)
        context = {'post': post[0]}
        return render(request, 'blog/post_detail.html', context)


class PostCreateView(View):
    @method_decorator(login_required())
    def get(self, request):
        post_form = ArticuloForm()
        context = {'form': post_form}
        return render(request, 'blog/post_create.html', context)

    @method_decorator(login_required())
    def post(self, request):
        message = None
        post_with_user = Articulo(created_by=request.user)
        post_form = ArticuloForm(request.POST, instance=post_with_user)

        if post_form.is_valid():
            post_form.save()
            post_form = ArticuloForm()
            message = '<p class="bg-success">Post creado correctamente</p>'

        context = {'form': post_form, 'message': message}
        return render(request, 'blog/post_create.html', context)
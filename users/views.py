from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    def get(self, request):
        error_message = ""
        return render(request, 'users/login.html', {'error': error_message})

    def post(self, request):
        """
        Presenta el formulario de login y gestiona el login de usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """

        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)

        if user is None:
            error_message = "Datos incorrectos"
        else:
            if user.is_active:
                django_login(request, user)
                return redirect(request.GET.get('next', "/"))
            else:
                error_message = "Cuenta de usuario inactiva"

        context = {'error': error_message}
        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)

        return redirect(request.GET.get('next', "/"))
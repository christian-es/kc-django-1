"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from blog.views import HomeView, BlogsView, PostView
from django.conf.urls import url
from django.contrib import admin
from users.views import LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^blogs/$', BlogsView.as_view()),

    url(r'^blogs/(?P<username>[a-zA-Z]+)$', PostView.as_view()),

    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', LogoutView.as_view()),
]
